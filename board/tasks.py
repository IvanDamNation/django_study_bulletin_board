from GameNotifPortal.celery import app

from .utils import send_to_author


@app.task
def send_author_task(user_email):
    send_to_author(user_email)
