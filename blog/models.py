from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pud_date = models.DateTimeField()
    body = models.TextField()
    imagem = models.ImageField(upload_to='images/')