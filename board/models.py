from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from taggit.managers import TaggableManager

class UserBoard(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='제목')
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    content = models.TextField(verbose_name='내용')
    created_dt = models.DateTimeField(auto_now_add=True)
    modified_dt = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(verbose_name='좋아요', default=0)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return '유저:{}, 제목:{}'.format(self.writer, self.title)

    def get_absolute_url(self):
        return reverse('board:detail', args=[self.slug])

    def board_save(self):
        self.save()

    class Meta:
        ordering = ['-created_dt']
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
