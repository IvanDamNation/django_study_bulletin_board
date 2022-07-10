from django.urls import path, include
from django.views.generic import TemplateView

from .views import Register, EmailVerify, MyLoginView, \
    CommentForAcceptList, personal_page_view, accept_commentary, \
    delete_commentary

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('',
         include('django.contrib.auth.urls')),
    path('invalid_verify/',
         TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'),
    path('verify_email/<uidb64>/<token>/',
         EmailVerify.as_view(),
         name='verify_email'),
    path('confirm_email/',
         TemplateView.as_view(template_name='registration/confirm_email.html'),
         name='confirm_email'),
    path('register/',
         Register.as_view(),
         name='register'),
    path('profile/',
         personal_page_view,
         name='profile'),
    path('profile/acceptation_list/',
         CommentForAcceptList.as_view(),
         name='acceptation_list'),
    path('<int:pk>/accept/',
         accept_commentary,
         name='comment_accept'),
    path('<int:pk>/delete/',
         delete_commentary,
         name='comment_delete')
]
