from django.contrib import admin
from django.urls import path
from pdvApp import views  # Substitua "app_name" pelo nome do seu app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_livros, name='home'),  # URL da página inicial que redireciona para a lista de livros
    path('cadastrar-livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('listar-livros/', views.listar_livros, name='listar_livros'),
    path('registrar-emprestimo/', views.registrar_emprestimo, name='registrar_emprestimo'),
    path('relatorio-emprestimos/', views.relatorio_emprestimos, name='relatorio_emprestimos'),
]
