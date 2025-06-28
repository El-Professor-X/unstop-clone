from django.urls import path
from .views import (event_list, event_detail, event_create, event_edit, event_delete, my_events)

urlpatterns = [
    path('', event_list, name='event_list'),
    path('<int:pk>/', event_detail, name='event_detail'),
    path('create/', event_create, name='event_create'),
    path('<int:pk>/edit/', event_edit, name='event_edit'),
    path('<int:pk>/delete/', event_delete, name='event_delete'),
    path('my-events/', my_events, name='my_events'),
]
