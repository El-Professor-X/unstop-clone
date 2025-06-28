from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

# ✅ List all public events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# ✅ Detail view for a single event
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
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
