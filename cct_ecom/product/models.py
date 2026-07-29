from django.db import models
from category.models import categories
from user.models import users


# Create your models here.
class products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class product_categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.ForeignKey( products, on_delete=models.CASCADE, related_name="product_categories")
    category_id = models.ForeignKey(categories,on_delete=models.CASCADE,related_name="product_categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class product_variants(models.Model):
    id = models.BigAutoField(primary_key=True)
    variant_name = models.CharField(max_length=255)
    variant_type = models.CharField(max_length=20)
    variant_value = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class product_reviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(users,on_delete=models.CASCADE,related_name="product_reviews")
    product_id = models.ForeignKey(products,on_delete=models.CASCADE,related_name="reviews")
    product_variant_id = models.ForeignKey(product_variants,on_delete=models.CASCADE,related_name="reviews")
    review_title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)