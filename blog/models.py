from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    body = models.TextField()
    imagem = models.ImageField(upload_to='images/')