from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import NewsForm
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


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'board/add_news.html'


class CommentList(ListView):
    model = Comment
    template_name = 'board/comments_list.html'
    context_object_name = 'commentaries'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com_list'] = Comment.objects.filter(news__pk=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        return Comment.objects.filter(news__pk=self.kwargs.get('pk'), accept=True)
