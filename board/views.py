from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import News, Category


# TODO
class NewsFeed(ListView):
    pass


# TODO
class NewsByCategory(ListView):
    pass


# TODO
class ViewNews(DetailView):
    pass


# TODO
class CreateNews(CreateView):
    pass
