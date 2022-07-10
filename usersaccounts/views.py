from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.views.generic import ListView

from board.models import Comment, News
from .tasks import send_sender_task
from .filters import CommentFilter
from .forms import UserCreationForm, AuthenticationForm
from .utils import send_email_for_verify


User = get_user_model()


class MyLoginView(LoginView):
    form_class = AuthenticationForm


class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.is_activated = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class CommentForAcceptList(ListView):
    model = Comment
    template_name = 'usersaccounts/acceptation_list.html'
    context_object_name = 'commentaries'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CommentFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        form = request.POST
        print(request.POST)
        if form.is_valid:
            obj = form.save(commit=False)
            obj.accept = True
            obj.save()

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Comment.objects.filter(news__author=self.request.user,
                                      accept=False)


def personal_page_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'usersaccounts/personal_page.html', context)


@login_required
def accept_commentary(request, pk):
    commentary = Comment.objects.get(pk=pk)
    commentary.accept = True
    commentary.save()
    for_send = {'email': commentary.sender.email}
    send_sender_task.delay(str(for_send['email']))

    return redirect('acceptation_list')


@login_required
def delete_commentary(request, pk):
    commentary = Comment.objects.get(pk=pk)
    commentary.delete()

    return redirect('acceptation_list')
