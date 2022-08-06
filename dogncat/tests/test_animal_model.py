from .test_base import TestBase, Animal
from django.core.exceptions import ValidationError
from parameterized import parameterized


class DognCatModelTeste(TestBase):
    def setUp(self) -> None:
        self.dogncat = self.make_animal()
        return super().setUp()

    def test_animal_title_if_has_more_than_65_chars(self):
        """Método averigua uma falhas proposital e levanta erro apenas se não falhar"""
        self.dogncat.description = 'A' * 280

        with self.assertRaises(ValidationError):
            self.dogncat.full_clean()

    @parameterized.expand([
        ('name', 65),
        ('description', 265),
        ('cidade', 25),
    ])
    def test_dogncat_fields_max_lenght(self, field, max_lenght):
        """Metodo averigua varias falhas propositais e levanta erro apenas se nao falhar
           O subtest não funciona com o Pytest de uma forma efetiva.
           Para termos infos precisas sobre qual teste falhou, melhor utilizar:
           $ python manage.py test
        """
        setattr(self.dogncat, field, 'A' * (max_lenght + 1))
        with self.assertRaises(ValidationError):
            self.dogncat.full_clean()

    def make_dogncat_no_default_field(self):
        """Método para ser utilizado em outros testes sem a adição de nenhum campo Default"""
        animal = Animal(
            type_of_animal='Tipo de ANimal',
            author=self.make_author(username='newuser'),
            name='Test Title',
            description='Descript Test',
            slug='test-slug-1000',
            castracao='Feita',
            porte='Médio',
            cidade='Maceio',)
        animal.full_clean()
        animal.save()
        return animal

    def test_dogncat_is_published_default(self):
        """Teste para confirmar o is_published > default = False"""
        animal = self.make_dogncat_no_default_field()
        self.assertFalse(
            animal.is_staff,
            msg='O is_published default é Falso, não podendo ser omitido esse field'
        )

    def test_animal_string_representation(self):
        """Testando a representação em String do nome do Animal"""
        needed = 'Testing Representation'
        self.dogncat.title = 'Testing Representation'
        self.dogncat.full_clean()
        self.dogncat.save()
        self.assertEqual(
            str(self.dogncat), needed,
            msg=f'Animal string representation must be {needed} but'
                f'{str(self.dogncat)} was received')
