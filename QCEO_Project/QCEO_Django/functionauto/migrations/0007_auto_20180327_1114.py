# Generated by Django 2.0.3 on 2018-03-27 02:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('functionauto', '0006_auto_20180327_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testreserve',
            name='starttime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='희망시작시간'),
        ),
    ]