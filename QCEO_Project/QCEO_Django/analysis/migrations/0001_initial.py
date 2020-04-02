# Generated by Django 3.0.5 on 2020-04-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestDefact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='번호')),
                ('item', models.CharField(max_length=10, verbose_name='대항목')),
                ('miditem', models.CharField(max_length=10, verbose_name='중항목')),
                ('subitem', models.CharField(max_length=10, verbose_name='소항목')),
                ('content', models.TextField(verbose_name='내용')),
                ('reference', models.TextField(verbose_name='참고항목')),
                ('case', models.FileField(blank=True, upload_to='case/', verbose_name='케이스 생성')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='등록')),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30, verbose_name='제품')),
                ('version', models.CharField(max_length=20, verbose_name='버전')),
                ('client', models.CharField(max_length=20, verbose_name='고객사')),
                ('content', models.TextField(verbose_name='결함현황')),
                ('list', models.TextField(blank=True, verbose_name='결함목록')),
                ('miss', models.TextField(verbose_name='점검시놓침')),
                ('impossible', models.TextField(verbose_name='점검시불가')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='등록')),
            ],
        ),
    ]
