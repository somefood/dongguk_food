# Generated by Django 2.2.4 on 2019-08-13 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.TextField(null=True, verbose_name='des'),
        ),
    ]
