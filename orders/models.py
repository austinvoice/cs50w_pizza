import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# Toppings one to many
class Topping(models.Model):
    topping_text = models.CharField(max_length=100, primary_key=True)
    pass

# Define major categories
class Category(models.Model):
    # define small and large sizes
    SMALL = 'S'
    LARGE = 'L'
    CATEGORY_SIZES = (
        (SMALL, 'Small'),
        (LARGE, 'Large'),
    )
    item_size = models.CharField(
        'size',
        max_length=1,
        choices=CATEGORY_SIZES,
        default=SMALL,
    )

    category_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # For pizza, many topping options
    toppings = models.ManyToManyField(Topping)

    # select new items custom method
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # return object on query
    def __str__(self):
        return self.category_text

# Define type within a category
class Type(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type_text = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    orders = models.IntegerField(default=0)

    # Return object on query
    def __str__(self):
        return self.type_text

    # Calculate total order value
    def order_value(self):
        value = self.price * self.orders
        return value
    #
    # # Calcul;ate total order size
    # def total_order(self):
    #     for i in range(20):
    #         value += self.price(pk=i) * self.orders(pk=i)
    #     return value

# Shopping Cart to track of items ordered
class Cart (models.Model):
    items = models.ForeignKey(Type, on_delete=models.CASCADE)
