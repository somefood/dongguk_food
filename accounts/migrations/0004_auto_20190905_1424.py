# Generated by Django 2.2.4 on 2019-09-05 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_agree'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': '프로필', 'verbose_name_plural': '프로필'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=30, null=True, verbose_name='거주 형태'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='agree',
            field=models.CharField(max_length=10, null=True, verbose_name='마게팅 동의'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='faFT',
            field=models.CharField(max_length=60, null=True, verbose_name='선호음식'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(max_length=30, null=True, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=30, null=True, verbose_name='전화번호'),
        ),
    ]