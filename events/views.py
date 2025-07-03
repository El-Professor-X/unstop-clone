from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event , EventRegistration
from .forms import EventForm
from django.contrib import messages
from events.models import Event
from datetime import datetime, timedelta
from django.utils.timezone import now
from django.db.models import Q
from events.models import Event


def home(request):
    events = Event.objects.all()
    today = now().date()

    # Get search query and category
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    # 🔍 Filter by search query
    if query:
        events = events.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    # 🕒 Filter by time category
    if category == 'live':
        events = events.filter(date__date=today)
    elif category == 'upcoming':
        events = events.filter(date__date__gt=today)
    elif category == 'past':
        events = events.filter(date__date__lt=today)

    return render(request, 'home.html', {
        'events': events,
        'query': query,
        'category': category,
    })

# ✅ List all public events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# ✅ Detail view for a single event
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# ✅ Create a new event
@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('my_events')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

# ✅ Edit an existing event
@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk, organizer=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('my_events')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

# ✅ Delete an event
@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, organizer=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('my_events')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

# ✅ View only the logged-in user's events
@login_required
def my_events(request):
    events = Event.objects.filter(organizer=request.user)
    return render(request, 'events/my_events.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        # Check if user already registered
        already_registered = EventRegistration.objects.filter(user=request.user, event=event).exists()
        if already_registered:
            messages.warning(request, "You are already registered for this event.")
        else:
            EventRegistration.objects.create(user=request.user, event=event)
            messages.success(request, "Registered successfully!")
        return redirect('event_detail', event_id=event.id)

    return render(request, 'events/event_detail.html', {'event': event})