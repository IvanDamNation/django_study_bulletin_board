from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category


# TODO
class NewsFeed(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context


# TODO
class NewsByCategory(ListView):
    pass


# TODO
class ViewNews(DetailView):
    pass


# TODO
class CreateNews(CreateView):
    pass
