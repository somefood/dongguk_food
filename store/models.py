from django.db import models
from django.shortcuts import reverse
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.conf import settings


class BaseModel(models.Model):
    created_dt = models.DateTimeField(auto_now_add=True)
    modified_dt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(BaseModel):
    CATEGORIES = (
        ('restaurant', '음식집'),
        ('bar', '술집'),
        ('cafe', '카페'),
    )
    name = models.CharField(max_length=50, verbose_name="가게명", unique=True)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for alias')
    location = models.CharField(max_length=100, blank=True, verbose_name="위치")
    phone_number = models.CharField(max_length=30, blank=True, verbose_name="연락처")
    description = models.TextField(blank=True, verbose_name="설명")
    store_image = models.ImageField(blank=True, upload_to="store/store_pic")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_stores')
    like_count = models.PositiveIntegerField(default=0)
    tags = TaggableManager(blank=True)
    category = models.CharField(max_length=10, choices=CATEGORIES)
    running_time = models.CharField(max_length=30, blank=True, verbose_name='영업시간')

    class Meta:
        verbose_name = '가게'
        verbose_name_plural = '가게'
        ordering = ['-like_count', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

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


class Comment(BaseModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.store} - {self.writer}'

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글'