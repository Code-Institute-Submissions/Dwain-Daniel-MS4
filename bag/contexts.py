from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from workouts.models import Workouts 

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag',{})

    for workouts_id, quantity in bag.items():
        workouts = get_object_or_404(Workouts, pk=workouts_id)
        total += quantity * workouts.price
        product_count += quantity
        bag_items.append({
            'workouts_id': workouts_id,
            'quantity': quantity,
            'workouts': workouts,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total
    }

    return context