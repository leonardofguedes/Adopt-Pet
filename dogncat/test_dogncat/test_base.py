from django.test import TestCase
from dogncat.models import Animal
from django.contrib.auth.models import User


class AnimalMixin:
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
                    author_data=None,
                    type_of_animal='Cachorro',
                    name='Test Title',
                    phone='9999999999',
                    description='Descript Test',
                    castracao='Feita',
                    porte='Médio',
                    cidade='Maceio',
                    is_staff=True):

        if author_data == None:
            author_data = {}

        return Animal.objects.create(
            author=self.make_author(**author_data),
            type_of_animal=type_of_animal,
            name=name,
            phone=phone,
            description=description,
            castracao=castracao,
            porte=porte,
            cidade=cidade,
            is_staff=is_staff,
        )

class TestBase(TestCase, AnimalMixin):
    def setUp(self) -> None:
        return super().setUp()