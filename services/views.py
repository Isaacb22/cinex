from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Service

# Create your views here.
def services(request):
    services = get_list_or_404(Service)
    return render(request, 'services/services.html', {'services':services})

def service(request, service_id, service_slug):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/service.html', {'service':service})