from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, "core/home.html")

def signup(request):
	if request.method == 'GET':
		return render(request, 'core/signup.html')
	elif request.method == 'POST':
		user = User()
		user.username = request.POST['username'] 
		user.email = request.POST['email']
		user.set_password(request.POST['password'])
		user.save()
		messages.add_message(request, messages.INFO, 'Usuario registrado correctamente, ya puede iniciar sesion')
		return HttpResponseRedirect('/accounts/login')


def contact(request):
	return render(request, "core/contact.html")
