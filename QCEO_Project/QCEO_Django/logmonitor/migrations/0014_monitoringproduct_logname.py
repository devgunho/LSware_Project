# Generated by Django 2.0.4 on 2018-05-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logmonitor', '0013_monitoringproduct_logpath'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoringproduct',
            name='logname',
            field=models.CharField(default='log.log', max_length=20, unique=True, verbose_name='운영체제'),
            preserve_default=False,
        ),
    ]