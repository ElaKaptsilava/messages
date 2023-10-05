# Generated by Django 3.2.21 on 2023-10-05 18:14

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=70), default=list, size=5)),
                ('cc', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=70), blank=True, default=list, size=None)),
                ('bcc', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=70), blank=True, default=list, size=None)),
                ('reply_to', models.EmailField(blank=True, default=None, max_length=70)),
                ('sent_date', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mailbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=300)),
                ('port', models.IntegerField(default=465)),
                ('login', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=20)),
                ('email_form', models.CharField(max_length=70)),
                ('use_ssl', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.AddField(
            model_name='email',
            name='mailbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.mailbox'),
        ),
        migrations.AddField(
            model_name='email',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.template'),
        ),
    ]
