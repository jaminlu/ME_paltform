# Generated by Django 2.1.2 on 2019-04-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idc', '0004_auto_20190409_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idc',
            name='dns',
        ),
        migrations.AddField(
            model_name='idc',
            name='dns_ip',
            field=models.CharField(blank=True, help_text='DNS', max_length=64, null=True, verbose_name='DNS'),
        ),
    ]
