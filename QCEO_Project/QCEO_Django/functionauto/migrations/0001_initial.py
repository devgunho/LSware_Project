# Generated by Django 3.0.5 on 2020-04-21 01:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autotest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=30, verbose_name='프로젝트')),
                ('testname', models.CharField(max_length=30, verbose_name='테스트명')),
                ('total', models.IntegerField(verbose_name='전체폴더개수')),
                ('starttime', models.DateTimeField(verbose_name='테스트시간')),
                ('path', models.CharField(blank=True, choices=[('/home/qceo/windowshare/Linux', 'Linux'), ('/home/qceo/windowshare/Solaris_intel', 'Solaris'), ('/home/qceo/windowshare/UNIX', 'UNIX')], max_length=100, verbose_name='경로')),
                ('file', models.FileField(blank=True, upload_to='', verbose_name='보고서')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='등록')),
            ],
        ),
        migrations.CreateModel(
            name='Testreserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='예약자명')),
                ('reservetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='예약시간')),
                ('starttime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='희망시작시간')),
                ('project', models.CharField(max_length=30, verbose_name='프로젝트명')),
                ('memo', models.TextField(blank=True, verbose_name='메모')),
                ('state', models.CharField(choices=[('예약', '예약'), ('접수', '접수'), ('진행', '진행'), ('완료', '완료')], default='예약', max_length=2, verbose_name='상태')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='등록')),
            ],
        ),
    ]
