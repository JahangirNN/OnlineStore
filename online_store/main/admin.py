from django.contrib import admin

# Register your models here.from django.contrib import admin
from . models import (
    Customer,
    Product,
    Category,
    Order
    )

admin.site.register(Category)

admin.site.register(Order)

admin.site.register(Product)

admin.site.register(Customer)