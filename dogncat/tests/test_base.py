from django.test import TestCase
from dogncat.models import Animal
from django.contrib.auth.models import User


class TestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_author(self,
                    first_name='user',
                    last_name='name',
                    username='username',
                    password='123456',
                    email='user@gmail.com',):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )
    def make_animal(self,
                    animal_type_data=None,
                    author_data=None,
                    title='Test Title',
                    description='Descript Test',
                    slug='test-slug',
                    castracao='Feita',
                    peso=5,
                    idade=5,
                    cidade='Maceio',
                    is_published=True):

        if author_data == None:
            author_data = {}

        return Animal.objects.create(
            type_of_animal=self.make_animal_type(**animal_type_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            castracao=castracao,
            peso=peso,
            idade=idade,
            cidade=cidade,
            is_published=is_published,
        )
