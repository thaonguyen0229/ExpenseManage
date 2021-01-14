from django.shortcuts import render
from django.utils import timezone

from .models import Spending, Earning, Repeat_event\



def home(request):
    if request.method == "POST":
        if request.POST['types'] == 'Earning':
            new = Earning()
            new.amount = request.POST['amount']
            new.description = request.POST['description']
            new.create_date = timezone.now()
            new.save()
        elif request.POST['types'] == 'Payment':
            new = Spending()
            new.amount = request.POST['amount']
            new.description = request.POST['description']
            new.create_date = timezone.now()
            new.save()

    spends = Spending.objects.all()
    earns = Earning.objects.all()
    repeat_events = Repeat_event.objects.all()
    return render(request, 'home.html', {
        'spends': spends,
        'earns': earns,
        'repeat_events': repeat_events,
    })
