from django import template
from services.models import Service

register = template.Library()

@register.simple_tag
def get_service_list():
    services = Service.objects.all()
    return services