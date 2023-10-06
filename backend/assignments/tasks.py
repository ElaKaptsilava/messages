from celery import shared_task
from django.core import mail
from django.utils import timezone

from .models import Email


@shared_task()
def sending_email(params):
    email = Email.objects.get(id=params['db_id'])
    with mail.get_connection():
        mail.EmailMessage(
            subject=email.template.subject, body=email.template.text,
            from_email=email.mailbox.email_form, to=email.to,
            cc=email.cc, bcc=email.bcc, reply_to=[email.reply_to],
            attachments=email.template.attachment,
        ).send()
        email.sent_date = timezone.now()
        email.save()
    return 'Done'
