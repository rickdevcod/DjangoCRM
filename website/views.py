from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
	# Verificar se esta fazendo loguin
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Autenticação
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Sucesso ao se conectar")
			return redirect('home')
		else:
			messages.success(request, "Usuário ou Senha incorretos, Tente Novamente!")
			return redirect('home')
	else:
		return render(request, 'home.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, "Você foi desconectado")
	return redirect('home')

def register_user(request):
	return render(request, 'register.html', {})