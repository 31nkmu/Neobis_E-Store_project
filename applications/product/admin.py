from django.contrib import admin

from applications.product.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
