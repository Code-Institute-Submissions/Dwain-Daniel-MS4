from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from workouts.models import Workouts

def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, workouts_id):
    """ Add a quantity of the specified product to the shopping bag """
    workouts = Workouts.objects.get(pk=workouts_id)
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if workouts_id in list(bag.keys()):
        bag[workouts_id] += quantity
    else:
        bag[workouts_id] = quantity
        messages.success(request,f'Added {workouts.name} to your bag')
    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, workouts_id):
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
            bag[workouts_id] = quantity
    else:
            bag.pop(workouts_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

 
def remove_from_bag(request, workouts_id):
    """remove the specified product from the bag"""
    try:
        bag = request.session.get('bag', {})

        bag.pop(workouts_id)


        request.session['bag'] = bag
        return HttpResponse(status=200)

    

    except Exception as e:
        return HttpResponse(status=500)
