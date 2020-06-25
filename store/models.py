from django.db import models
from django.shortcuts import reverse
from taggit.managers import TaggableManager

class Store(models.Model):
    CATEGORIES = (
        ('restaurant', '음식집'),
        ('bar', '술집'),
        ('cafe', '카페'),
    )
    name = models.CharField(max_length=50, verbose_name="가게명")
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for alias')
    location = models.CharField(max_length=100, blank=True, verbose_name="위치")
    phone_number = models.CharField(max_length=30, blank=True, verbose_name="연락처")
    description = models.TextField(blank=True, verbose_name="설명")
    store_image = models.ImageField(blank=True, upload_to="store/store_pic")
    created_dt = models.DateTimeField(auto_now_add=True)
    modified_dt = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(verbose_name='좋아요', default=0)
    tags = TaggableManager(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORIES)

    class Meta:
        verbose_name = '가게'
        verbose_name_plural = '가게'
        ordering = ['likes', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:detail', args=[self.slug])

class Menu(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="가게명")
    name = models.CharField(max_length=50, verbose_name="메뉴")
    description = models.CharField(max_length=50, blank=True, verbose_name="설명")
    food_image = models.ImageField(blank=True, upload_to="store/menu_pic")

    class Meta:
        verbose_name = '메뉴'
        verbose_name_plural = '메뉴'

    def __str__(self):
        return "{} - {}".format(self.store, self.name)