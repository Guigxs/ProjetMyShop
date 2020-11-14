from django.shortcuts import render
from cart.cart import Cart
from .models import Order
from .forms import OrderCreateForm
from shop.recommender import Recommender
from shop.models import Product
from neomodel import db

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order(**form.data)
            order.save()
            order.paid="1"
            for item in cart:
                order.products.connect(item["product"], {'quantity':item['quantity']})

            order.save()
            print(order.products.all())
            product_ids = list(cart.cart.keys())
            print(product_ids)
            products = []
            for id in product_ids:
                query = f"match (a) where ID(a) = {id} return a"
                result, meta = db.cypher_query(query)
                products.append(Product.inflate(result[0][0]))

            r = Recommender()
            r.products_bought([products])

            # clear the cart
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
