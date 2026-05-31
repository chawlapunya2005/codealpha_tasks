from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, Order, OrderItem

def home(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/home.html', {'products': products, 'categories': categories})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})

def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            item_total = product.price * quantity
            total += item_total
            cart_items.append({'product': product, 'quantity': quantity, 'total': item_total})
        except Product.DoesNotExist:
            pass
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart
    messages.success(request, "Item added to cart!")
    return redirect('cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')

def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    qty = int(request.POST.get('quantity', 1))
    if qty > 0:
        cart[str(product_id)] = qty
    else:
        cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect('cart')
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            item_total = product.price * quantity
            total += item_total
            cart_items.append({'product': product, 'quantity': quantity, 'total': item_total})
        except Product.DoesNotExist:
            pass
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        order = Order.objects.create(user=request.user, address=address, phone=phone, total_price=total)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['product'].price)
        request.session['cart'] = {}
        messages.success(request, f"Order #{order.id} placed successfully!")
        return redirect('order_success', order_id=order.id)
    return render(request, 'store/checkout.html', {'cart_items': cart_items, 'total': total})

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'store/my_orders.html', {'orders': orders})
