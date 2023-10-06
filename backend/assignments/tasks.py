from celery import shared_task
from django.core import mail
from django.utils import timezone

from .models import Email


@shared_task()
def sending_email(params):
    email = Email.objects.get(id=params['db_id'])
    emails = (
        (email.template.subject, email.template.text, email.reply_to, email.to),
        (email.template.subject, email.template.text.join('\nCopy'), email.reply_to, email.cc),
    )
    result = mail.send_mass_mail(emails)
    email.sent_date = timezone.now()
    email.save()
