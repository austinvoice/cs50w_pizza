import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

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

    # Return object on query
    def __str__(self):
        return self.type_text
