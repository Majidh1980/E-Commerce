from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart

@login_required
def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.status = 'Pending'
            payment.save()
            messages.success(request, 'پرداخت شما با موقیت انجام شد!')
            return redirect('payment_success')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})

@login_required
def payment_success(request):
    return render(request, 'payment_success.html')

@login_required
def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()
    return render(request, 'checkout.html', {'cart_products': cart_products, 'quantities': quantities, 'total': total})
