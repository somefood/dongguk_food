from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30, blank=True)
    description = models.TextField(verbose_name='des', null=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    menu = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.menu