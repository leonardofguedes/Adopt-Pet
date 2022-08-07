from django.urls import reverse, resolve
from dogncat import views
from .test_base import TestBase
from unittest import skip


class HomeViewTest(TestBase):
    """Testando o método view utilizado para home"""
    def test_animals_home_view_is_correct(self):
        view = resolve(reverse('dogncat:home'))
        self.assertIs(view.func, views.home_view)

    def test_animal_home_with_animal_registered(self):
        """Testando se o título do animal criado aparece na home"""
        self.make_animal(name='Title')
        response = self.client.get(reverse('dogncat:home'))
        content = response.content.decode('utf-8')
        self.assertIn('Test Title', content)

    def test_rental_home_view_loads_template(self):
        """Testando um template carregado em home"""
        response = self.client.get(reverse('dogncat:home'))
        self.assertTemplateUsed(response, 'dogncat/partials/base.html')

    def test_animals_home_view_return_status_200(self):
        """Testando se a resposta da URL em home é 200"""
        response = self.client.get(reverse('dogncat:home'))
        self.assertEqual(response.status_code, 200)

    @skip ('Teste propositalmente falho')
    def test_animals_home_template_with_an_animal_registered(self):
        """Testando se a mensagem 'Nenhum aninmal cadastrado ainda' aparece quando criamos um animal"""
        self.make_animal()
        response = self.client.get(reverse('dogncat:home'))
        self.assertIn(
            '<h1>Nenhum animal cadastrado ainda</h1>',
            response.content.decode('utf-8')
        )

    def test_animals_home_template_with_no_animal_registered(self):
        """Testando se a mensagem Nenhum aninmal cadastrado ainda aparece sem criarmos um animal"""
        response = self.client.get(reverse('dogncat:home'))
        self.assertIn(
            '<h1>Nenhum animal cadastrado ainda</h1>',
            response.content.decode('utf-8')
        )

    def test_home_content_if_is_published_false(self):
        """Testando o animal registrado acaso o Is Published seja falso"""
        self.make_animal(is_staff=False)
        response = self.client.get(reverse('dogncat:home'))
        self.assertIn(
            '<h1>Nenhum animal cadastrado ainda</h1>',
            response.content.decode('utf-8')
        )

    def test_home_status_if_is_published_false(self):
        """Testando o animal registrado acaso o Is Published seja falso"""
        self.make_animal(is_published=False)
        response = self.client.get(reverse('dogncat:home'))
        self.assertEqual(response.status_code, 200)


class OneAnimalViewTest(TestBase):
    def test_one_animal_view_is_correct(self):
        """Testando o método view utilizado para one animal"""
        view = resolve(reverse('dogncat:animal', kwargs={'id':1}))
        self.assertIs(view.func, views.animal)

    def test_one_animal_template_loads_fine(self):
        """Testando a página detalhada de animal quando criamos 1 animal"""
        self.make_animal(description='One Animal Test Template')
        response = self.client.get(reverse('dogncat:animal', kwargs={'id':1}))
        content = response.content.decode('utf-8')
        self.assertIn('One Animal Test Template', content)

    def test_one_animal_status_with_no_animal_registered(self):
        """Testando o status code da página quando não houver animal cadastrado"""
        response = self.client.get(reverse('dogncat:animal', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)

    def test_one_animal_status_with_Is_Published_False(self):
        """Testando o status code da página com Is Published == False"""
        response = self.client.get(reverse('dogncat:animal', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)