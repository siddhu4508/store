from django.contrib import admin

from .models import Product, Cpu_cooler, Mother_board

admin.site.register(Product)
admin.site.register(Cpu_cooler)
admin.site.register(Mother_board)
