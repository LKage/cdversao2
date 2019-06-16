from django.shortcuts import render, redirect, get_object_or_404
from .forms import PessoaForm
from .models import PessoaModel


# Create your views here.

def list_pessoa(request):
    form = PessoaModel.objects.all() ##ler a tabela pessoa
    # form = ContatoModel.objects.all() ##ler a tabela contato
    context = {
        'form': form,
    }
    return render(request, 'listar.html', context)

def insert_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_pessoa')
    context = {
        'form': form,
    }
    return render(request, 'inserir.html', context)

def update_pessoa(request, id):
    pessoa = get_object_or_404(PessoaModel, pessoa_id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('list_pessoa')
    context = {
        'form': form,
    }
    return render(request, 'editar.html', context)


def delete_pessoa(request, id):
    pessoa = get_object_or_404(PessoaModel, pessoa_id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('list_pessoa')
    context={
        'form': form,
    }
    return render(request, 'deletar.html', context)


def view_pessoa(request, id):
    pessoa = get_object_or_404(PessoaModel, pessoa_id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    if request.method == 'POST':
        return redirect('list_pessoa')
    context={
        'form': form,
    }
    return render(request, 'consultar.html', context)
