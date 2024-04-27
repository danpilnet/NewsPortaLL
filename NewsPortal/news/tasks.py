from celery import shared_task
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives







@shared_task()
def sending(preview, pk, title, subscribers):
    html_content = render_to_string(
        'message.html',
        {
            'text':preview,
            'title':title,
            'link':f'{settings.SITE_URL}/{pk}/'
        }
    )


    message_tasks = EmailMultiAlternatives(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )


