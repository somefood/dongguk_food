from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, null=True, verbose_name='닉네임',)
    phone_number = models.CharField(max_length=30, null=True, verbose_name='전화번호',)
    address = models.CharField(max_length=30, null=True, verbose_name='거주 형태',)
    faFT = models.CharField(max_length=60, null=True, verbose_name='선호음식',)
    agree = models.CharField(max_length=10, null=True, verbose_name='마게팅 동의')

    class Meta:
        verbose_name = '프로필'
        verbose_name_plural = '프로필'

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()