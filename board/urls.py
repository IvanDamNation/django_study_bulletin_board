from django.urls import path


from .views import NewsFeed, NewsByCategory, ViewNews, CreateNews


# TODO
urlpatterns = [
    path('', NewsFeed.as_view(), name='home'),

]
