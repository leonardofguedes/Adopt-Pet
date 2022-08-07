from django.test import TestCase
from django.urls import reverse



class AnimalsURLTest(TestCase):
    """Testando a URL de Home"""
    def test_animals_home_url_is_correct(self):
        home_url = reverse('dogncat:home')
        self.assertEqual(home_url, '/')

    def test_one_animals_url_is_correct(self):
        """Testando a URL de um animal específico"""
        url = reverse('dogncat:animal', kwargs={'id': 200})
        self.assertEqual(url, '/animal/200/')

    def test_animals_by_type_url_is_correct(self):
        """Testando a URL do filtro por tipo de animal"""
        url = reverse('dogncat:animal-type', kwargs={'type_id': 1})
        self.assertEqual(url, '/animal-type/1/')

