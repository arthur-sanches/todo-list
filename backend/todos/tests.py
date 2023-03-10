from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='first todo', body='a body here')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_title = f'{todo.title}'
        self.assertEquals(expected_object_title, 'first todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_body = f'{todo.body}'
        self.assertEquals(expected_object_body, 'a body here')
