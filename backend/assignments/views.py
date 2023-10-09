from django.db import models
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException

from .models import Email, Template, Mailbox
from .serializers import TemplateSerializer, EmailSerializer, MailBoxSerializer
from rest_framework import viewsets
from django.db import transaction
from .tasks import sending_email
import django_filters


class EmailFilterSet(django_filters.FilterSet):
    class Meta:
        model = Email
        fields = {'date': ['gt', 'lte', 'contains'],
                  'sent_date': ['gt', 'lte', 'contains']}
        filter_overrides = {
            models.DateTimeField: {
                'filter_class': django_filters.DateFilter,
            }
        }


class TemplateViewSet(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()

    def get_object(self):
        template = super().get_object()
        template.last_update = timezone.now()
        template.save()
        return template


class MailBoxViewSet(viewsets.ModelViewSet):
    serializer_class = MailBoxSerializer
    queryset = Mailbox.objects.all()

    def get_object(self):
        mailbox = super().get_object()
        mailbox.last_update = timezone.now()
        mailbox.save()
        return mailbox


class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmailFilterSet

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save()
                instance.save()
                params = {'db_id': instance.id}
                if instance.is_active:
                    transaction.on_commit(lambda: sending_email.delay(params))
        except Exception as ex:
            raise APIException(str(ex))
