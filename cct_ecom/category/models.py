from django.db import models

# Create your models here.
class categories(models.Model):
     id = models.BigAutoField(primary_key=True)
     title = models.CharField(max_length=255, unique=True)
     slug = models.SlugField(max_length=255, unique=True)
     description = models.TextField(blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)