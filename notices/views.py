from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Notice

# Create your views here.

def notices(request):
    notices = get_list_or_404(Notice)
    return render(request, 'notices/notices.html', {'notices':notices})

def notice(request, notice_id, notice_slug):
    notice = get_object_or_404(Notice, id=notice_id)
    return render(request, 'notices/notice.html', {'notice':notice})
