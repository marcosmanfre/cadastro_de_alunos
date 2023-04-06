from django.shortcuts import render

from .models import Aluno


def home(request):
    alunos = Aluno.objects.all()

    context = {
        'alunos': alunos,
    }
    return render(request, 'register/pages/home.html',context)

