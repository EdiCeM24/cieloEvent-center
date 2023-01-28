from django.contrib import admin

from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'price')
    

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Offer, OfferAdmin)

admin.site.register(Product, ProductAdmin)