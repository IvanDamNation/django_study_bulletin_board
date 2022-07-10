from django.core.mail import send_mail

from GameNotifPortal.settings import DEFAULT_FROM_EMAIL


def send_to_author(user_email):
    send_mail(
        'Your news got new comment',
        'Check it on your account on portal and accept or delete it',
        DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
