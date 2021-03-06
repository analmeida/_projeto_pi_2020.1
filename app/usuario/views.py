from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth, messages
from medico.models import Medico
from atendente.models import Atendente
from consulta.models import Consulta
from datetime import datetime, date

def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=user).exists():
            user = auth.authenticate(request, username=user, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Senha inválida.')
        else:
            messages.error(request, 'Usuário/Senha inválidos.')
            return render(request, 'usuarios/login.html')
    
    
    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)   
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        dados =  get_dados(request)
        if dados['tipo'] == 1:
            lst_consultas = Consulta.objects.filter(medico=dados['usuario'])
            lst_consultas = separa_data_hr(lst_consultas)
            dados['consultas'] = lst_consultas
    return render(request, 'usuarios/index.html', dados)



#---------------------------------------------------------------
# UTILS 
#---------------------------------------------------------------
def verifica_usuario(request):
    tipo_usuario = None
    if Medico.objects.filter(usuario=request.user):
        tipo_usuario = 1   
    if Atendente.objects.filter(usuario=request.user):
        tipo_usuario = 2

    return tipo_usuario

def get_usuario(request):
    usuario = None
    if verifica_usuario(request) == 1:
        usuario = get_object_or_404(Medico, usuario=request.user)

    if verifica_usuario(request) == 2:  
        usuario = get_object_or_404(Atendente, usuario=request.user)

    return usuario

def get_dados(request):
    dados = {'usuario': get_usuario(request),'tipo': verifica_usuario(request)}   
    return dados

def separa_data_hr(lst_consultas):
    #Separando data e hora.
    for consulta in lst_consultas:
        hora = datetime.strftime(consulta.data, '%H:%M')
        data = datetime.strftime(consulta.data, '%d/%m/%Y')
        consulta.data = data
        consulta.hora = hora
        
    return lst_consultas