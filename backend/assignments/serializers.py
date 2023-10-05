from .models import *
from rest_framework import serializers


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class MailBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        read_only_fields = ("id", "sent_date")
        fields = '__all__'
