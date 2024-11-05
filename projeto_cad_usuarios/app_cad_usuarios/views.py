from django.shortcuts import render
from .models import Usuario
def home(request):
    return render (request,'usuarios/home.html')

def usuarios (request):
    #Salva os dados da tela para o banco de dados 
    novo_usuario= Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #exibir todos os usuarios já cadastrado dentro de uma nova pagina
    usuarios ={
        'usuarios': Usuario.objects.all()
    }
    #Retorna os dados para a pagina listagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)

  