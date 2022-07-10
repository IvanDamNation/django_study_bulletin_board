from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewsForm, CommentForm
from .models import News, Category, Comment
from .tasks import send_author_task


class NewsFeed(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/news_detail.html'
    paginate_by = 10
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'

    def get_success_url(self, **kwargs):
        return reverse_lazy('view_news', kwargs={'pk': self.get_object().id})


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'board/add_news.html'

    def post(self, request, *args, **kwargs):
        form = NewsForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = self.request.user
            obj.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CommentList(ListView):
    model = Comment
    template_name = 'board/comments_list.html'
    context_object_name = 'commentaries'
    paginate_by = 20
    form_class = CommentForm
    success_msg = 'Comment was sent to author, wait for accept'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        news_pk = self.kwargs.get('pk')
        news = News.objects.get(pk=news_pk)
        sender = self.request.user
        text = request.POST['text']
        comment = Comment(news=news, sender=sender, text=text)

        if CommentForm.is_valid:
            messages.success(request, self.success_msg)
            comment.save()
            send_author_task.delay(comment.news.author)

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Comment.objects.filter(news__pk=self.kwargs.get('pk'), accept=True)
