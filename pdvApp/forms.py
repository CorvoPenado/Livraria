from django import forms
from .models import Livro, Emprestimo

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'nome_pessoa', 'dias_emprestimo']
        widgets = {
            'livro': forms.Select(attrs={'class': 'form-control'}),
            'nome_pessoa': forms.TextInput(attrs={'class': 'form-control'}),
            'dias_emprestimo': forms.NumberInput(attrs={'class': 'form-control'}),
        }
