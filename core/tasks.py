from celery import shared_task
from core.models import *
from django.core.mail import send_mail

@shared_task
def send_mail(to_email):
    subject = "Price Reached for Set Alert"
    text_content = "Price Reached for Set Alert"
    from_email = "ayush.jain.11032002@gmail.com"
    send_mail(subject, text_content, from_email, [to_email])
