from django.contrib import admin
from .models import Products, Offer

class ProductAdmin(admin.ModelAdmin):
    list_display=("name", "stock", "price")

class OfferAdmin(admin.ModelAdmin):
    list_display=("code", "discount")

admin.site.register(Products, ProductAdmin)
admin.site.register(Offer, OfferAdmin)