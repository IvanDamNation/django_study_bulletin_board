from django.urls import path

from .views import NewsFeed, NewsByCategory, ViewNews, CreateNews, CommentList

urlpatterns = [
    path('',
         NewsFeed.as_view(),
         name='home'),
    path('category/<int:category_id>/',
         NewsByCategory.as_view(),
         name='category'),
    path('<int:pk>/',
         ViewNews.as_view(),
         name='view_news'),
    path('add-news/',
         CreateNews.as_view(),
         name='add_news'),
    path('<int:pk>/commentaries/',
         CommentList.as_view(),
         name='view_comments'),
]
