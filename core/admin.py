from django.contrib import admin

from .models import Product , Category , SubCategory , Service

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug','product_type']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

admin.site.register(Category) 
admin.site.register(SubCategory)
admin.site.register(Service)

