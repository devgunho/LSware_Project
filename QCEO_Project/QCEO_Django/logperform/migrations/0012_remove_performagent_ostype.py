# Generated by Django 2.0.4 on 2018-05-29 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logperform', '0011_auto_20180529_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performagent',
            name='ostype',
        ),
    ]