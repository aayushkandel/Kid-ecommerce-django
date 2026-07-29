from django.db import models
from user.models import users
from cart.models import cart,cart_items
from product.models import products, product_variants

# Create your models here.
class orders(models.Model):

    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(users,on_delete=models.CASCADE,related_name="orders")
    cart_id = models.ForeignKey(cart,on_delete=models.CASCADE,related_name="orders")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_status = models.CharField( max_length=20,  default="pending")
    remarks = models.TextField(blank=True, null=True)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class order_items(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey(products,on_delete=models.CASCADE,related_name="order_items")
    product_variant_id = models.ForeignKey(product_variants,on_delete=models.CASCADE,related_name="order_items")
    order_id = models.ForeignKey(orders,on_delete=models.CASCADE,related_name="items")
    cart_item_id = models.ForeignKey(cart_items,on_delete=models.CASCADE,related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(users,on_delete=models.CASCADE,related_name="payments")
    order_id = models.ForeignKey(orders,on_delete=models.CASCADE,related_name="payments")
    payment_method = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    transaction_id = models.CharField(max_length=100,blank=True,null=True)
    payment_status = models.CharField(max_length=20,default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
