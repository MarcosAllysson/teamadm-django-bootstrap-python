from django import forms
from .models import ComandoModel


class ComandoModelForm(forms.ModelForm):
    """
    Definiando classe pro cadastrao de um novo comando.
    """
    class Meta:
        # referencia ao models
        model = ComandoModel

        # quais campos têm que ser preenchidos
        fields = ['desenvolvedor', 'tecnologia', 'comando', 'descricao']
