from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from events.models import Event
from django.conf import settings
from django.conf.urls.static import static
from events.views import home
from django.conf import settings
from django.conf.urls.static import static


def homepage(request):
    events = Event.objects.all().order_by('-date')[:6]  # Only latest 6 events
    return render(request, 'home.html', {'events': events})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('api/', include('api.urls')),
    path('', homepage, name='home'),
  # 👈 Add this
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
