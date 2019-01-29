from django.shortcuts import render
from .models import Post

def services(request):
	consulta = request.GET.get('Search', None)
	if consulta:
		posts = Post.objects.filter(title__icontains = consulta)
	else:
		posts = Post.objects.all()
	return render(request, "services/services.html", {'posts':posts})