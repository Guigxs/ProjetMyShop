from shop.models import Product
from coupons.models import Coupon
from datetime import datetime
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator
from neomodel import (config, StructuredNode, StructuredRel, StringProperty, DateTimeFormatProperty, RelationshipTo, RelationshipFrom, FloatProperty, IntegerProperty)

config.DATABASE_URL = 'bolt://neo4j:interpreters-flashes-soap@54.160.119.107:35012'


class Contains(StructuredRel):
    quantity = IntegerProperty()


class Order(StructuredNode):
    first_name = StringProperty(max_length=50)
    last_name = StringProperty(max_length=50)
    email = StringProperty()
    address = StringProperty(max_length=250)
    postal_code = StringProperty(max_length=20)
    city = StringProperty(max_length=100)
    created = StringProperty(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated = StringProperty(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    paid = StringProperty(default="0")
    coupon = RelationshipTo("coupons.models.Coupon", "USE")
    products = RelationshipTo("shop.models.Product", "CONTAINS", model=Contains)
    discount = StringProperty()

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        price = 0
        for item in self.products.all():
            price  = self.products.relationship(item).quantity * item.price
        
        total_cost = price - price * (float(self.discount)/100)
        return total_cost


# class OrderItem(StructuredNode):
#     order = models.ForeignKey(Order,
#                               related_name='items',
#                               on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,
#                                 related_name='order_items',
#                                 on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return str(self.id)

#     def get_cost(self):
#         return self.price * self.quantity

# class Order(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     address = models.CharField(max_length=250)
#     postal_code = models.CharField(max_length=20)
#     city = models.CharField(max_length=100)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     paid = models.BooleanField(default=False)
#     coupon = models.ForeignKey(Coupon,
#                                related_name='orders',
#                                null=True,
#                                blank=True,
#                                on_delete=models.SET_NULL)
#     discount = models.IntegerField(default=0,
#                                    validators=[MinValueValidator(0),
#                                                MaxValueValidator(100)])

#     class Meta:
#         ordering = ('-created',)

#     def __str__(self):
#         return f'Order {self.id}'

#     def get_total_cost(self):
#         total_cost = sum(item.get_cost() for item in self.items.all())
#         return total_cost - total_cost * \
#             (self.discount / Decimal(100))


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order,
#                               related_name='items',
#                               on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,
#                                 related_name='order_items',
#                                 on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return str(self.id)

#     def get_cost(self):
#         return self.price * self.quantity
