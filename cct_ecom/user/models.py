from django.db import models

# Create your models here.
class users(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255, null=True)
    email=models.EmailField(max_length=255, null=True)
    phone=models.IntegerField(max_length=20, default=None)
    billing_address=models.CharField(max_length=255, default=None)
    shipping_address=models.CharField(max_length=255, default=None)
    username=models.CharField(max_length=100, null=True, unique=True)
    password=models.CharField(max_length=255, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)