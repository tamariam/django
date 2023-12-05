from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    def test_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
           

    def  test_edit(self):
        item = Item.objects.create(name='Test todo item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')
        
     