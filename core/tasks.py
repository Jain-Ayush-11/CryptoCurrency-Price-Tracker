from celery import shared_task
from core.models import *
from django.core.mail import send_mail

@shared_task
def send_price_alerts(to_email_list, price):
    send_email.delay(to_email_list, price)
    for email in to_email_list:
        print(f"Price Reached for Alert at {price} for {email}")

@shared_task
def send_email(to_email_list, price):
    subject = f"Price Reached for Alert at {price}"
    text_content = f"Price Reached for Alert at {price}"
    from_email = "ayush.jain.11032002@gmail.com"
    send_mail(subject, text_content, from_email, to_email_list)
