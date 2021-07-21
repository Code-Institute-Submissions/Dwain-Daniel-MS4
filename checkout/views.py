from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag, have a look at our workouts and try again")
        return redirect(reverse('workouts'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J4SFiEoVoZEWSIattAYrkxYbQ2HtxK31gLytQ5mZ6KHIcM2LQKByJFdEzPlZhLjnMBet4jj4SfkXacRaiedamKe002dItqMds',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)