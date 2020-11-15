from neomodel import (config, StructuredNode, StringProperty, DateTimeFormatProperty, RelationshipTo, RelationshipFrom, FloatProperty)
from django.core.validators import MinValueValidator, \
                                   MaxValueValidator

config.DATABASE_URL = 'bolt://neo4j:interpreters-flashes-soap@54.160.119.107:35012'


class Coupon(StructuredNode):
    code = StringProperty(max_length=50,
                            unique_index=True)
    valid_from = StringProperty()
    valid_to = StringProperty()
    discount = StringProperty()
    active = StringProperty()
    orders = RelationshipFrom("orders.models.Order", "USE")

    def __str__(self):
        return self.code

# class Coupon(models.Model):
#     code = models.CharField(max_length=50,
#                             unique=True)
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     discount = models.IntegerField(
#                    validators=[MinValueValidator(0),
#                                MaxValueValidator(100)])
#     active = models.BooleanField()

#     def __str__(self):
#         return self.code
