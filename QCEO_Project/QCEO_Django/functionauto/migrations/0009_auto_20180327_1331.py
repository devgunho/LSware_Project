# Generated by Django 2.0.3 on 2018-03-27 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functionauto', '0008_auto_20180327_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testreserve',
            name='state',
            field=models.CharField(choices=[('예약', '예약'), ('접수', '접수'), ('진행', '진행'), ('완료', '완료')], default='예약', max_length=2, verbose_name='상태'),
        ),
    ]