from django.shortcuts import redirect, render
from register.models import Aluno
from .models import Aluno


def home(request):
    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }
    return render(request, 'home.html', context)


def adicionar(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        secao = request.POST.get('secao')

        alunos = Aluno(
            nome=nome,
            sobrenome=sobrenome,
            secao=secao

        )
        alunos.save()
        return redirect('home')


def editar(request):
    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }
    return redirect(request, 'home.html', context)


def salvar(request, id):
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        secao = request.POST.get('secao')

        alunos = Aluno(
            id=id,
            nome=nome,
            sobrenome=sobrenome,
            secao=secao,

        )
        alunos.save()
        return redirect('home')

    return redirect(request, 'home.html')


def deletar(request, id):
    alunos = Aluno.objects.filter(id=id)
    alunos.delete()
    context = {
        'alunos': alunos,
    }
    return redirect('home')
