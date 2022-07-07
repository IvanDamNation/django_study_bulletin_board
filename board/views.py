from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin


from .forms import NewsForm, CommentForm
from .models import News, Category, Comment


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
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True)


class ViewNews(FormMixin, DetailView):
    model = News
    context_object_name = 'news_item'
    form_class = CommentForm
    success_msg = 'Comment sent to author, wait for accept'

    def get_success_url(self, **kwargs):
        return reverse_lazy('view_news', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.news = self.get_object()
        self.object.sender = self.request.user
        self.object.save()
        return super().form_valid(form)


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'board/add_news.html'


class CommentList(ListView):
    model = Comment
    template_name = 'board/comments_list.html'
    context_object_name = 'commentaries'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_pk'] = self.kwargs.get('pk')
        return context

    def get_queryset(self):
        return Comment.objects.filter(news__pk=self.kwargs.get('pk'), accept=True)
