from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
	if request.method == 'GET':
		return render(request, 'registration/signup.html')
	elif request.method == 'POST':
		user = User()
		user.username = request.POST['username'] 
		user.email = request.POST['email']
		user.set_password(request.POST['password'])
		user.save()
		return HttpResponse('hola')


