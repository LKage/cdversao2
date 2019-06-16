from django import forms
from .models import PessoaModel
from .models import EstadoModel
from .models import CidadeModel
from .models import ContatoModel

class PessoaForm(forms.ModelForm):
    pessoa_nome = forms.CharField(required=True, label="Nome")
    estado_nome = forms.CharField(required=True, label="Estado")
    cidade_nome = forms.CharField(required=True, label="Cidade")
    pessoa_logradouro = forms.CharField(required=True, label="Logradouro")
    pessoa_numero = forms.CharField(required=True, label="Número")
    contato_telefone = forms.CharField(required=True, label="Telefone")

    class Meta:
        model = PessoaModel
        fields = [
            'pessoa_nome',
            'estado_nome',
            'cidade_nome',
            'pessoa_logradouro',
            'pessoa_numero',
            'contato_telefone',
        ]
        
        
class ContatoForm(forms.ModelForm):
    
    contato_telefone = forms.CharField(label="Telefone")
    pessoa = forms.ModelChoiceField(queryset=PessoaModel.objects.all(), label="Contato")

    class Meta:
        model = ContatoModel
        fields = ['contato_telefone']


class EstadoForm(forms.ModelForm):

    estado_nome = forms.CharField(label="Estado")
    estado = forms.ModelChoiceField(queryset=EstadoModel.objects.all(), label="Estado")

    class Meta:
        model = EstadoModel
        fields = ['estado_nome']


class CidadeForm(forms.ModelForm):
    cidade_nome = forms.CharField(label="Cidade")
    cidade_nome = forms.ModelChoiceField(queryset=CidadeModel.objects.all(), label="Cidade")

    class Meta:
        model = CidadeModel
        fields = ['cidade_nome']

