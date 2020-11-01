from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.FileField()
    found = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])