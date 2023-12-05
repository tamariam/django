from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):
    def test_done_defaults_false(self):
        item = Item.objects.create(name='test todo item')
        self.assertFalse(item.done)
        