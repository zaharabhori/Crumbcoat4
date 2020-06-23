from django.db import models

# Create your models here.
class images(models.Model):
    img = models.ImageField(upload_to = 'pics')
    choice = models.CharField(max_length=50)