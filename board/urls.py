from django.urls import path


from .views import NewsFeed, NewsByCategory, ViewNews, CreateNews


urlpatterns = [
    path('',
         NewsFeed.as_view(),
         name='home'),
    path('category/<int:category_id>/',
         NewsByCategory.as_view(),
         name='category'),


]
