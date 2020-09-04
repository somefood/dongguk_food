# Generated by Django 3.0.5 on 2020-07-06 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='제목')),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('like_users', models.ManyToManyField(related_name='like_boards', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '게시판',
                'verbose_name_plural': '게시판',
                'ordering': ['-created_dt'],
            },
        ),
    ]