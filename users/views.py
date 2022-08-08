from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from dogncat.models import Animal


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            return redirect('cadastro')
        if not email.strip():
            return redirect('cadastro')
        if senha!= senha2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request, 'users/pages/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'O usuário não existe')
            return redirect('login')

    return render(request, 'users/pages/login.html')

def logout(request):
    auth.logout(request)
    return redirect('dogncat:home')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        animais = Animal.objects.order_by('-created_at').filter(author=id)
        dados = {
            'animais' : animais
        }
        return render(request, 'users/pages/dashboard.html', dados)
    else:
        return redirect('login')


def newpet(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        description = request.POST['caracteristicas']
        cidade = request.POST['cidade']
        porte = request.POST['porte']
        castracao = request.POST['castracao']
        type_of_animal = request.POST['tipodeanimal']
        cover = request.FILES['foto_pet']
        user = get_object_or_404(User, pk=request.user.id)
        animal = Animal.objects.create(
            author=user,
            name=nome,
            description=description,
            cidade=cidade,
            cover=cover,
            type_of_animal=type_of_animal,
            porte=porte,
            castracao=castracao)
        if animal:
            animal.save()
            messages.success(request, 'Animal cadastrado com sucesso')
            return redirect('dashboard')
        else:
            print('mensagem')
    else:
        return render(request, 'users/pages/pet_add_form.html')

def dashboard_delete(request, id=None):
    if id is not None:
        animal = Animal.objects.filter(pk=id).first()
        animal.delete()
        messages.success(request, 'Animal deletado')
        return redirect(reverse('dashboard'))
    else:
        messages.error(request, 'Error')
        return redirect(reverse('dashboard'))