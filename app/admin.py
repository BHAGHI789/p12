from django.contrib import admin

# Register your models here.
from .models import Product
class Productadmin(admin.ModelAdmin):
    list_display=["id","name","price"]
admin.site.register(Product,Productadmin)