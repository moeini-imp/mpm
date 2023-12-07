# tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_push_notification(user_email, message):

    send_mail('Push Notification', message, 'from@example.com', [user_email])
