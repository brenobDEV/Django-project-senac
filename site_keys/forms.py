from django import forms

from .models import Key


class KeysForm(forms.ModelForm):

    class Meta:
        model = Key

        fields = [
            "titulo",
            "plataforma",
            "preco",
            "preco_anterior",
            "descricao",
            "imagem_url",
            "estoque",
            "ativo",
        ]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome do jogo",
                }
            ),

            "plataforma": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: PC, Steam",
                }
            ),

    
            "preco": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "preco_anterior": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                    "min": "0",
                }
            ),

            "descricao": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Descrição do jogo",
                }
            ),

            "imagem_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://...",
                }
            ),

            "estoque": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                }
            ),

            "ativo": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }