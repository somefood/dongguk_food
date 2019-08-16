from django.db import models

class UserBoard(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    mail = models.CharField(max_length=50, blank=True)
    memo = models.CharField(max_length=50, blank=True)
    hits = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.subject)