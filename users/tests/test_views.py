from django.urls import resolve, reverse
from users.views import *
from django.test import TestCase


class ViewTest(TestCase):
    def test_register_view_function(self):
        resolved = resolve(reverse('cadastro'))
        self.assertIs(resolved.func, cadastro)

    def test_login_view_function(self):
        resolved = resolve(reverse('login'))
        self.assertIs(resolved.func, login)