from django.contrib import auth, messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from receitas.models import Receita
# Create your views here.


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O nome não pode ficar em branco')
            return redirect('cadastro')
        
        if campo_vazio(email):
            messages.error(request, 'O email não pode ser vazio')

        if senhas_diferentes(senha, senha2):
            messages.error(request, 'Senhas não são iguais')
            print('Senhas não são iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            print('Usuário já cadastrado')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            print('Usuário já cadastrado')
            return redirect('cadastro')


        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        messages.success(request, 'Cadastro Realizado com Sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email = email).values_list('username',flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa = id)

        dados = {
            'receitas' : receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(
            pessoa=user, 
            nome_receita=nome_receita, 
            ingredientes=ingredientes, 
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            categoria=categoria,
            rendimento=rendimento,
            foto_receita=foto_receita)

        receita.save()

        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')

def campo_vazio(campo):
    return not campo.strip()

def senhas_diferentes(senha, senha2):
    return senha != senha2
