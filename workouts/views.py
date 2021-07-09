from django.shortcuts import render
from .models import Workouts

# Create your views here.

def all_workouts(request):
    """ A view to show all products, including sorting and search queries """

    workouts = Workouts.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts.html', context)