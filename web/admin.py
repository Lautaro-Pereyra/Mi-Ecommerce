from django.contrib import admin

# Register your models here.

from .models import Categoria,Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_de_registro')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','categoria')
    list_editable =('precio',)