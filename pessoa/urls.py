
from django.contrib import admin
from django.urls import path
from . import views

##http://localhost:8000/pessoa/incluir
##http://localhost:8000/pessoa/listar
urlpatterns = [
    ## URL     ## nome função               chamada interna
    path('inserir', views.insert_pessoa, name='insert_pessoa'),
    path('alterar/<int:id>', views.update_pessoa, name='update_pessoa'),
    path('excluir/<int:id>', views.delete_pessoa, name='delete_pessoa'),
    path('consultar/<int:id>', views.view_pessoa, name='view_pessoa'),
    path('listar', views.list_pessoa, name='list_pessoa'),
]
