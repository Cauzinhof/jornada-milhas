from django.contrib import admin
from .models import Depoimento, Destino

class Depoimentos(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ['nome']

admin.site.register(Depoimento, Depoimentos)

class Destinos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco')
    list_display_links = ('id', 'nome')
    search_fields = ['nome']

admin.site.register(Destino, Destinos)