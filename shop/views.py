from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product
from .recommender import Recommender
from .viewers import Viewer
from django.views.decorators.cache import cache_page

# @cache_page(5*60) # set 5 min cache
def product_list(request, category_slug=None):
    category = None
    categories = Category.nodes.all()
    products = Product.nodes.filter(available="1")
    if category_slug:
        category = Category.nodes.filter(slug=category_slug)[0]
        products = category.products
        print(category.name)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = Product.nodes.filter(slug=slug, available="1")
    print(product.all())
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    
    total_views = str(Viewer.getViewers(id))
    Viewer.addViewer(id)
    print(product.all()[0].category.all())
    return render(request,
                  'shop/product/detail.html',
                  {'product': product.all()[0],
                    'category': product.all()[0].category.all()[0],
                   'cart_product_form': cart_product_form,
                    'recommended_products': recommended_products,
                   'total_views': total_views})
