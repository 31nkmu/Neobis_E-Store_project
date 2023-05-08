from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)


class Product(models.Model):
    STATUS = (
        ('on_sale', 'on sale'),
        ('out_of_stock', 'out of stock')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=88)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.PositiveIntegerField(default=10)
    status = models.CharField(max_length=50, choices=STATUS, default='on_sale')
    orders_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
