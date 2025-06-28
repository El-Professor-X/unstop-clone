from .views import user_dashboard
from django.urls import path
urlpatterns = [ path('', user_dashboard, name='dashboard') ]
