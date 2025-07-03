from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from events.models import EventRegistration
from events.models import Event

@login_required
def user_dashboard(request):
    registrations = EventRegistration.objects.filter(user=request.user)
    return render(request, 'dashboard/user_dashboard.html', {'registrations': registrations})

@login_required
def organizer_dashboard(request):
    events = Event.objects.filter(organizer=request.user)
    data = []
    for event in events:
        registrations = EventRegistration.objects.filter(event=event).count()
        data.append({
            'event': event,
            'registrations': registrations
        })

    return render(request, 'dashboard/organizer_dashboard.html', {'data': data})

@login_required
def organizer_dashboard(request):
    # Filter only events created by logged-in user
    my_events = Event.objects.filter(organizer=request.user)
    return render(request, 'dashboard/organizer_dashboard.html', {
        'my_events': my_events
    })