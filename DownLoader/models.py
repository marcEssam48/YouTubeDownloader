from django.db import models

# Create your models here.
class links(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=1000)
    auther = models.CharField(max_length=1000)
    VideoName = models.CharField(max_length=1000)
    date_download = models.DateTimeField(auto_now_add=True)
