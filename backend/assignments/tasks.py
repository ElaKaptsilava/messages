from celery import shared_task
from django.core.mail import get_connection, EmailMessage
from django.utils import timezone
from backend.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER

from .models import Email, Mailbox


@shared_task()
def sending_email(params):
    email = Email.objects.get(id=params['db_id'])
    mailbox = Mailbox.objects.get(id=email.mailbox.id)
    backend_connection = get_connection(host=mailbox.host, port=mailbox.port,
                                        username=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD,
                                        use_ssl=mailbox.use_ssl)
    with backend_connection:
        EmailMessage(
            subject=email.template.subject, body=email.template.text,
            from_email=email.mailbox.email_form, to=email.to,
            cc=email.cc, bcc=email.bcc, reply_to=[email.reply_to],
            attachments=email.template.attachment, connection=backend_connection
        ).send()
        email.sent_date = timezone.now()
        email.save()
