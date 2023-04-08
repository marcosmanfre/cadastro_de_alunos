from django.shortcuts import redirect, render

from register.models import Aluno

from .models import Aluno


def home(request):
    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }
    return render(request, 'register/pages/home.html', context)


def adicionar(request):
    if request.method == "POST":
        registro_aluno = request.POST.get('registro_aluno')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        secao = request.POST.get('secao')

        alunos = Aluno(
            registro_aluno=registro_aluno,
            nome=nome,
            sobrenome=sobrenome,
            secao=secao

        )
        alunos.save()
        return redirect('register')
