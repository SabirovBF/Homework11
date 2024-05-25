from django.test import TestCase
from django.test import Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.animal = models.Animal.objects.create(
            name='Кабан',
            type='mammal',
            population=15,
            is_rare=True
        )

    def test_index(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)

    def test_detail_animal(self):
        response = self.client.get(f'/index/{self.animal.id}')
        self.assertEqual(response.status_code, 404)

    def text_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)

    def test_animal(self):
        response = self.client.get('/animals/')
        self.assertEqual(response.status_code, 200)

    def text_index_class(self):
        response = self.client.get('/index_class/')
        self.assertEqual(response.status_code, 200)

    def text_form(self):
        response = self.client.get('/for_example/')
        self.assertEqual(response.status_code, 200)
