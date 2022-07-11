from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20, default="")

class Shop(models.Model):
    shop_name = models.CharField(max_length=20, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shop", null=True)


class Product(models.Model):
    product_name = models.CharField(max_length=20, default="")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products", null=True)

class Review(models.Model):
    body = models.CharField(max_length=255, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", null=True)

