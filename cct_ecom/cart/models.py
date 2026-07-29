from django.db import models
from user.models import users
from product.models import product_variants, products
# Create your models here.

class cart(models.Model):
    id=models.BigAutoField(primary_key=True)
    user_id=models.ForeignKey(users, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class cart_items(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey(products,on_delete=models.CASCADE,related_name="cart_items")
    product_variant_id = models.ForeignKey(product_variants,on_delete=models.CASCADE,related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)