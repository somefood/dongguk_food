from django.db import models
from django.contrib.auth.models import User

class UserBoard(models.Model):
    title = models.CharField(max_length=50, blank=True, verbose_name='제목')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    created_date = models.DateTimeField(null=True, blank=True)
    mail = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=50, blank=True)
    hits = models.IntegerField(null=True, blank=True, verbose_name='좋아요')

    def __str__(self):
        return '유저:{}   제목:{}'.format(self.writer, self.title)

    def board_save(self):
        self.save()

    class Meta:
        verbose_name = '게시판'
        verbose_name_plural = '게시판'
