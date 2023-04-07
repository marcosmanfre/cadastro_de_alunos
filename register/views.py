from django.shortcuts import render, redirect
from register.models import Aluno

from .models import Aluno


def home(request):
    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }
    return render(request, 'register/pages/home.html',context)


def adicionar(request):
    if request.method == "POST":
        registro = request.POST.get('registro')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        secao = request.POST.get('secao')

        alunos = Aluno(
            registro = registro,
            nome = nome,
            sobrenome = sobrenome,
            secao = secao

        )
        alunos.save()
        return redirect('register/pages/home.html')
