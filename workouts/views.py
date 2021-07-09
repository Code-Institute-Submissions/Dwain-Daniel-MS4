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


def workouts_detail(request, workouts_id):
 
    workouts = get_object_or_404(Workouts, pk=workouts_id)

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts_detail.html', context)

