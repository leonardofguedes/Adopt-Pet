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

    def test_dashboard_view_function(self):
        resolved = resolve(reverse('dashboard'))
        self.assertIs(resolved.func, dashboard)

    def test_logout_view_function(self):
        resolved = resolve(reverse('logout'))
        self.assertIs(resolved.func, logout)