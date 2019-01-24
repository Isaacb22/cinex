from django.urls import path
from . import views

urlpatterns = [
    path('', views.notices, name='notices'),
    path('<int:notice_id>/<slug:notice_slug>/', views.notice, name='notice'),
    ]

