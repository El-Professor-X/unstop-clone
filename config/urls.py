from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('api/', include('api.urls')),
    path("", lambda request: render(request, "home.html")),

  # 👈 Add this
]
