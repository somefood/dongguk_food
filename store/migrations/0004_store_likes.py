# Generated by Django 3.0.5 on 2020-06-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200602_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]