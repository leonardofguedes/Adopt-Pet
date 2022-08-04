from django.shortcuts import render

def cadastro(request):
    return render(request, 'users/pages/cadastro.html')

def login(request):
    return render(request, 'users/pages/login.html')

def logout(request):
    pass

def dashboard(request):
    pass
