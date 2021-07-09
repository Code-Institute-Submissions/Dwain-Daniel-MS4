from django.shortcuts import render, get_object_or_404
from .models import Workouts

# Create your views here.

def all_workouts(request):
    """ A view to show all products, including sorting and search queries """

    workouts = Workouts.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts.html', context)


def workout_detail(request, workout_id):
    """ A view to show all products, including sorting and search queries """

    workouts = get_object_or_404(Workouts, pk=workout_id)

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts.html', context)

