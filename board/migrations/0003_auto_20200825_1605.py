# Generated by Django 3.0.5 on 2020-08-25 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_dt',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='updated',
            new_name='modified_dt',
        ),
    ]