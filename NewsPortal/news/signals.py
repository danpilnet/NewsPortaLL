# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from django.conf import settings
# from.models import PostCategory
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
#
#
#
#
#
# def send_message(preview, pk, title, subscribers, pole_ar_ne):
#     html_content = render_to_string(
#         'message.html',
#         {
#             'text': preview,
#             'title': title,
#             'link': f'{settings.SITE_URL}/news/{pk}/',
#             'pole_ar_ne': pole_ar_ne
#         }
#
#     )
#
#
#     message = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#
#
#     )
#
#     message.attach_alternative(html_content, 'text/html')
#     message.send()
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_subsribes(sender, instance,**kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribes_emails = []
#         for category in categories:
#             subscribes_emails += [sub.email for sub in category.subscribers.all()]
#
#         send_message(instance.preview(),
#                      instance.pk,
#                      instance.zagolovok,
#                      subscribes_emails,
#                      instance.pole_ar_ne,)
#
#
#
