from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from bag.contexts import bag_contents


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    order_form = OrderForm()
    templte = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': stripe_checkout_session['client_secret'],
    }
    return render(request, templte, context)
