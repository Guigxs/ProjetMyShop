from django.db import models
from django.urls import reverse
from datetime import datetime

from neomodel import (config, StructuredNode, StringProperty, DateTimeFormatProperty, RelationshipTo, RelationshipFrom, FloatProperty)

config.DATABASE_URL = 'bolt://neo4j:interpreters-flashes-soap@54.160.119.107:35012'


class Category(StructuredNode):
    name = StringProperty(max_length=200, index=True)
    slug = StringProperty(max_length=200)
    products = RelationshipFrom("Product", "PART_OF")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])
    


class Product(StructuredNode):
    category = RelationshipTo('Category', "PART_OF")
    name = StringProperty(max_length=200, index=True)
    slug = StringProperty(max_length=200, index=True)
    image = StringProperty()
    description = StringProperty()
    price = FloatProperty()
    available = StringProperty(default="1")
    created = StringProperty(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    updated = StringProperty(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    orders = RelationshipFrom("orders.models.Order", "CONTAINS")
    # created = DateTimeFormatProperty(default_now=True, format='%Y-%m-%d %H:%M:%S')
    # updated = DateTimeFormatProperty(default_now=True, format='%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
    
    def getID(self):
        return self.id



# class Category(models.Model):
#     name = models.CharField(max_length=200,
#                             db_index=True)
#     slug = models.SlugField(max_length=200,
#                             unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'category'
#         verbose_name_plural = 'categories'

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('shop:product_list_by_category',
#                        args=[self.slug])


# class Product(models.Model):
#     category = models.ForeignKey(Category,
#                                  related_name='products',
#                                  on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d',
#                               blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ('name',)
#         index_together = (('id', 'slug'),)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('shop:product_detail',
#                        args=[self.id, self.slug])
