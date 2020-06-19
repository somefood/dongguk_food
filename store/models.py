from django.db import models
from django.shortcuts import reverse

class Store(models.Model):
    name = models.CharField(max_length=50, verbose_name="가게명")
    location = models.CharField(max_length=100, verbose_name="위치")
    phone_number = models.CharField(max_length=30, blank=True, verbose_name="연락처")
    description = models.TextField(blank=True, verbose_name="설명")
    store_image = models.ImageField(blank=True, upload_to="store/store_pic")
    created_dt = models.DateTimeField(auto_now_add=True)
    modified_dt = models.DateTimeField(auto_now=True)
    likes = models.IntegerField()

    class Meta:
        verbose_name = '가게'
        verbose_name_plural = '가게'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:detail', args=[self.id])

class Menu(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="가게명")
    name = models.CharField(max_length=50, verbose_name="메뉴")
    description = models.CharField(max_length=50, verbose_name="설명")
    votes = models.IntegerField(default=0, verbose_name="투표수")
    food_image = models.ImageField(blank=True, upload_to="store/menu_pic")

    class Meta:
        verbose_name = '메뉴'
        verbose_name_plural = '메뉴'
        ordering = ['-votes',]

    def __str__(self):
        return "{} - {}".format(self.store, self.name)