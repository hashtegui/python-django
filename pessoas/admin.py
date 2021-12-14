from typing import List
from django.contrib import admin

# Register your models here.
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id','nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 50


admin.site.register(Pessoa,ListandoPessoas)