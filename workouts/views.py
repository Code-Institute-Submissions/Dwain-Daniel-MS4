from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Workouts, Category
from .forms import WorkoutsForm

# Create your views here.

def all_workouts(request):
    """ A view to show all products, including sorting and search queries """

    workouts = Workouts.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            workouts = workouts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('workouts'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            workouts = workouts.filter(queries)

    context = {
        'workouts': workouts,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'workouts/workouts.html', context)


def workouts_detail(request, workouts_id):
 
    workouts = get_object_or_404(Workouts, pk=workouts_id)

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts_detail.html', context)


def add_workouts(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = WorkoutsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a new workout!')
            return redirect(reverse('add_workouts'))
        else:
            messages.error(request, 'Failed to add new workout. Please ensure the form is valid.')
    else:
        form = WorkoutsForm()
        
    template = 'workouts/add_workouts.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_workouts(request, workouts_id):
    """ Edit a product in the store """
    workouts = get_object_or_404(Workouts, pk=workouts_id)
    if request.method == 'POST':
        form = WorkoutsForm(request.POST, request.FILES, instance=workouts)
        if form.is_valid():
            workouts = form.save()
            messages.success(request, 'Successfully updated workout!')
            return redirect(reverse('workouts_detail', args=[workouts.id]))
        else:
            messages.error(request, 'Failed to update workouts. Please ensure the form is valid.')
    else:
        form = WorkoutsForm(instance=workouts)
        messages.info(request, f'You are editing {workouts.name}')

    template = 'workouts/edit_workouts.html'
    context = {
        'form': form,
        'workouts': workouts,
    }

    return render(request, template, context)


def delete_workouts(request, workouts_id):
    """ Delete a product from the store """
    workouts = get_object_or_404(Workouts, pk=workouts_id)
    workouts.delete()
    messages.success(request, 'Workout deleted!')
    return redirect(reverse('workouts'))
