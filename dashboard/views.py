from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from events.models import EventRegistration

@login_required
def user_dashboard(request):
  regs = EventRegistration.objects.filter(user=request.user).select_related('event')
  return render(request, 'dashboard/dashboard.html', {'regs': regs})
