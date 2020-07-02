from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.conf import settings

def generate_unique_slug(klass, field):
    """
    return unique slug if origin slug is exist.
    """
    origin_slug = slugify(field, allow_unicode=True)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug


class UserBoard(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='제목')
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    content = models.TextField(verbose_name='내용')
    created_dt = models.DateTimeField(auto_now_add=True)
    modified_dt = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_boards')
    like_count = models.PositiveIntegerField(default=0)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return '{}-{}'.format(self.writer, self.title)

    def get_absolute_url(self):
        return reverse('board:detail', args=[self.slug])

    def save(self, **kwargs):
        if self.slug:
            if slugify(self.title, allow_unicode=True) != self.slug:
                self.slug = generate_unique_slug(UserBoard, self.title)
        else:
            self.slug = generate_unique_slug(UserBoard, self.title)
        super().save(**kwargs)

    class Meta:
        ordering = ['-created_dt']
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
