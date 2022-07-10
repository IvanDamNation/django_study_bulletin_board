from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from GameNotifPortal.settings import DEFAULT_FROM_EMAIL
from board.models import News
from usersaccounts.models import User


def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string(
        'registration/verify_email.html',
        context=context,
    )
    email = EmailMessage(
        'Verify email',
        message,
        to=[user.email],
    )
    email.send()


def send_to_sender(user_email):
    send_mail(
        'Your news got new comment',
        'Check it on your account on portal and accept or delete it',
        DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )


def send_newsletter():
    all_mails = []
    news_list = []

    for one_user in User.objects.all():
        all_mails.append(one_user.email)

    week_number_last = timezone.now().isocalendar()[1] - 1

    for news in News.objects.filter(created_at__week=week_number_last).values('pk'):
        news_list.append(f'http://127.0.0.1:8000/{news.get("pk")}')

    send_mail(
        'Check your feed!',
        f'There is some fresh news from game portal: {news_list}',
        DEFAULT_FROM_EMAIL,
        [all_mails],
        fail_silently=True,
    )
