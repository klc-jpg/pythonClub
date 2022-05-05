# Generated by Django 4.0.4 on 2022-05-05 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=255)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.CharField(max_length=255)),
                ('meetinglocation', models.CharField(max_length=255)),
                ('meetingagenda', models.TextField(blank=True, help_text='Add meeting agenda details', null=True)),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcename', models.CharField(max_length=255)),
                ('resourcetype', models.CharField(max_length=255)),
                ('resourceurl', models.URLField(blank=True, null=True)),
                ('resourcedescription', models.TextField(blank=True, help_text='Add details about this resource', null=True)),
                ('resourceentrydate', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'resources',
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutestext', models.TextField(blank=True, null=True)),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meetingid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Club.meeting')),
            ],
            options={
                'verbose_name_plural': 'meeting_minutes',
                'db_table': 'meetingminutes',
            },
        ),
        migrations.CreateModel(
            name='EventOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=255)),
                ('eventlocation', models.CharField(max_length=255)),
                ('eventdate', models.DateField()),
                ('eventtime', models.CharField(max_length=255)),
                ('eventdescription', models.TextField(blank=True, help_text='Add details about the event', null=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events_one',
                'db_table': 'eventone',
            },
        ),
    ]
