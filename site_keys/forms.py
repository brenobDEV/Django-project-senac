from django import forms
from .models import Keys


class KeysForm(forms.ModelForm):

    class Meta:
        model = Keys
        fields = ['titulo', 'plataforma', 'estoque', 'descricao', 'imagem_url',]