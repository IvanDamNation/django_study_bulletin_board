from celery import shared_task

from GameNotifPortal.celery import app

from .utils import send_to_sender, send_newsletter


@app.task
def send_sender_task(user_email):
    send_to_sender(user_email)


@shared_task
def send_newsletter_every_week():
    send_newsletter()
