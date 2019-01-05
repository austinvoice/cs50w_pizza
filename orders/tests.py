from django.test import TestCase
from django.test import Client
from django.utils import timezone

from .models import Category, Type

# Create your tests here.
# Test for index page to show
class IndexModelTest(TestCase):

    # Set up data for testing
    def setUp(self):

        # Create categories
        a1 = Category.objects.create(category_text="Category", pub_date=timezone.now())

        # Create Types
        Type.objects.create(category_id=1, type_text="Type", orders=1, price=1)

    def test_index(self):
        c = Client()
        response =c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["category_list"].count(), 1)

    def test_valid_type(self):
        a = Category.objects.get(pk=1)

        c = Client()
        response = c.get("/{a.id}/")
        self.assertEqual(response.status_code, 200)
