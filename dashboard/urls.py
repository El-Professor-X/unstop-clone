from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='dashboard'),
    path('organizer/', views.organizer_dashboard, name='organizer_dashboard'),
]
