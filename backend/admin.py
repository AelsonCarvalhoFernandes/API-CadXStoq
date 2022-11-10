from django.contrib import admin
from .models import Entrada, Saida, Produtos

class Produto(admin.ModelAdmin):
    list_display = ('name', 'quant', 'price')

class Entradas(admin.ModelAdmin):
    list_display = ('name', 'quant', 'price', 'created', 'updated', 'regis_por')
    list_display_links = None

class Saidas(admin.ModelAdmin):
    list_display = ('name', 'quant', 'price', 'created', 'updated', 'regis_por')
    list_display_links = None


admin.site.register(Produtos, Produto)
admin.site.register(Entrada, Entradas)
admin.site.register(Saida, Saidas)