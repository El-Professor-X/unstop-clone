from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('api/', include('api.urls')),

  # 👈 Add this
]
