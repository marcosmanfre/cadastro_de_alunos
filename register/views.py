from django.shortcuts import render


def home(request):
    return render(request, 'register/pages/home.html')
    
