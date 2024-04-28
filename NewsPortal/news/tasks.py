from celery import shared_task
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from celery.schedules import crontab








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


    message_tasks.attach_alternative(html_content, 'text/html')
    message_tasks.send()




@shared_task()
app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'action',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}