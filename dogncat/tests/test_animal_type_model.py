from django.core.exceptions import ValidationError
from .test_base import TestBase, Animal


class DognCatModelTeste(TestBase):
    def setUp(self) -> None:
        self.animal_type = self.make_animal_type(name='Animal Type Test')
        return super().setUp()

    def test_animal_type_string_representation(self):
        """Testando a representação em String do Animal Type"""
        self.assertEqual(
            str(self.animal_type),
            self.animal_type.name
        )

    def test_animal_type_model_is_65_chars(self):
        """Testando o max lenght do name de Animal Type"""
        self.animal_type.name = 'a' * 66
        with self.assertRaises(ValidationError):
            self.animal_type.full_clean()