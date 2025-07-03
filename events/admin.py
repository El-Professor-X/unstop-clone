from django.contrib import admin
from .models import Event, EventRegistration

admin.site.register(EventRegistration)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'date', 'category')

admin.site.register(Event, EventAdmin)
