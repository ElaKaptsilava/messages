from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Mailbox(models.Model):
    host = models.CharField(max_length=300)
    port = models.IntegerField(default=465)
    login = models.CharField(max_length=70)
    password = models.CharField(max_length=20)
    email_form = models.CharField(max_length=70)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)

    @property
    def sent(self):
        return

class Template(models.Model):
    subject = models.CharField(max_length=50)
    text = models.TextField()
    attachment = models.FileField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject


class Email(models.Model):
    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    to = ArrayField(models.EmailField(max_length=70), size=5, default=list)
    cc = ArrayField(models.EmailField(max_length=70), default=list, blank=True)
    bcc = ArrayField(models.EmailField(max_length=70), default=list, blank=True)
    reply_to = models.EmailField(default=None, max_length=70, blank=True)
    sent_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
