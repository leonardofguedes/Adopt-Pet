from django.test import TestCase
from django.urls import reverse


class UsersURLTest(TestCase):
    def test_users_register_url_is_correct(self):
        url = reverse('cadastro')
        self.assertEqual(url, '/user/cadastro/')

    def test_users_login_url_is_correct(self):
        url = reverse('login')
        self.assertEqual(url, '/user/login/')

    def test_users_dashboard_url_is_correct(self):
        url = reverse('dashboard')
        self.assertEqual(url, '/user/dashboard/')

"""
urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
]
"""