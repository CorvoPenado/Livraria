from django.shortcuts import render, redirect
from .models import Livro, Emprestimo
from .forms import LivroForm, EmprestimoForm

def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'pdvApp/cadastrar_livro.html', {'form': form})

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'pdvApp/listar_livros.html', {'livros': livros})

def registrar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relatorio_emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'pdvApp/registrar_emprestimo.html', {'form': form})

def relatorio_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'pdvApp/relatorio_emprestimos.html', {'emprestimos': emprestimos})
