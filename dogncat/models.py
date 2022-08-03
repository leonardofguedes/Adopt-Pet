from django.db import models
from django.contrib.auth.models import User


class Type_of_animal(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Animal(models.Model):
    CASTRACAO = (
        ('Feita', 'Feita'),
        ('Pendente', 'Pendente'),
        ('Indefinido', 'Não informado')
    )
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=265)
    slug = models.SlugField(unique=True)
    castracao = models.CharField(choices=CASTRACAO, blank=False, null=False, default='U', max_length=15)
    peso = models.IntegerField()
    idade = models.IntegerField()
    cidade = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='animals/covers/%Y/%m/%d/', blank=True, default='')
    type_of_animal = models.ForeignKey(
        Type_of_animal, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.title

class Photo(models.Model):
    """main_photo = models.ImageField(null=True, blank=True, upload_to ='animals/main_photos/%Y/%m/%d/')
    second_photo = models.ImageField(null=True, blank=True, upload_to ='animals/second_photos/%Y/%m/%d/')
    third_photo = models.ImageField(null=True, blank=True, upload_to ='animals/third_photos/%Y/%m/%d/')
    fourth_photo = models.ImageField(null=True, blank=True, upload_to='animals/fourth_photos/%Y/%m/%d/')"""
    animal = models.ForeignKey(Animal, default=None, on_delete=models.CASCADE)
    images = models.FileField(default=None, upload_to='images/')

    def __str__(self):
        return self.animal.title