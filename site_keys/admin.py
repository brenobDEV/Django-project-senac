from django.contrib import admin
from .models import Key


@admin.register(Key)
class KeysAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'plataforma',
        'preco',
        'estoque',
        'ativo',
    )

    list_filter = (
        'plataforma',
        'ativo',
    )

    search_fields = (
        'titulo',
        'descricao',
    )