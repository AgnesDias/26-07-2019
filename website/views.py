from django.shortcuts import render
from website.models import Pessoa

# Create your views here.

def index(request):
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        Pessoa.nome = request.POST.get('nome')
        Pessoa.sobrenome = request.POST.get('sobrenome')
        Pessoa.email = request.POST.get('email')
        Pessoa.genero = request.POST.get('genero')
        pessoa.save()
        contexto = {'msg': 'Usuario Cadastrado!'} #contexto não está funcionando

    return render(request, 'index.html', contexto)

def sobre(request):
    pessoa = Pessoa.objects.filter(ativo=True).all()
    contexto = {'pessoas':pessoa

    }
    return render(request, 'sobre.html', contexto)
