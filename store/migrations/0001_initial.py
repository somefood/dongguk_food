# Generated by Django 3.0.5 on 2020-06-01 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='가게명')),
                ('location', models.CharField(max_length=100, verbose_name='위치')),
                ('phone_number', models.CharField(blank=True, max_length=30, verbose_name='연락처')),
                ('description', models.TextField(blank=True, verbose_name='설명')),
            ],
            options={
                'verbose_name': '가게',
                'verbose_name_plural': '가게',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='메뉴')),
                ('description', models.CharField(max_length=50, verbose_name='설명')),
                ('votes', models.IntegerField(default=0, verbose_name='투표수')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store', verbose_name='가게명')),
            ],
            options={
                'verbose_name': '메뉴',
                'verbose_name_plural': '메뉴',
                'ordering': ['-votes'],
            },
        ),
    ]
