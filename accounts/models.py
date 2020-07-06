from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True, verbose_name='닉네임')
    phone_number = models.CharField(max_length=30, unique=True, verbose_name='전화번호')