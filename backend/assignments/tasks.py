from .models import *
from celery import shared_task
from django.core.mail import send_mail
from backend import settings


@shared_task()
def sending_email(params):
    email = Email.objects.get(id=params['db_id'])

    if len(email.to) > 0:
        send_mail(
            subject=email.template.subject,
            message=email.template.text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email.to + email.cc,
            fail_silently=True
        )
        print('Send copy to bcc')

        if len(email.bcc) > 0:
            send_mail(
                subject=email.template.subject,
                message=email.template.text.join('\n There is no need to reply to the message.'),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=email.bcc,
                fail_silently=True
            )
            print('Send copy to bcc')
    email.sent_date = timezone.now()
    email.save()
