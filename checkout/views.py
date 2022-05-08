from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.config import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

def checkout(request):
    """Checkout view."""
    # stripe public and secret keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_method(*args, **kwargs)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency= settings.STRIPE_CURRENCY,
    )
    order_form = OrderForm()
    # if the is no public key, return an error
    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing. "
                                  "Add it to your settings.")

    templte = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,
    }
    return render(request, templte, context)
