from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import APIException

from .serializers import *
from rest_framework import viewsets
from django.db import transaction
from .tasks import sending_email
import django_filters


class EmailFilterSet(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='date', lookup_expr='gt')

    class Meta:
        model = Email
        fields = ['date']


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
                transaction.on_commit(lambda: sending_email.delay(params))
        except Exception as ex:
            raise APIException(str(ex))