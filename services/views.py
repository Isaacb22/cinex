from django.shortcuts import render
from .models import Post

def services(request):
	posts = Post.objects.all(	)
	return render(request, "services/services.html", {'posts':posts})