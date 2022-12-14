from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    name = models.CharField(max_length=65)
    description = models.CharField(max_length=265)
    castracao = models.CharField(blank=False, null=False, default='U', max_length=25)
    porte = models.CharField(max_length=65, null=True)
    cidade = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=True)
    phone = models.IntegerField()
    cover = models.ImageField(upload_to='animals/covers/%Y/%m/%d/', blank=True, null=True, default='')
    photo_detail = models.ImageField(upload_to='animals/photo_detail/%Y/%m/%d/', blank=True, default='')
    photo_detail_two = models.ImageField(upload_to='animals/photo_detail_two/%Y/%m/%d/', blank=True, default='')
    photo_detail_three = models.ImageField(upload_to='animals/photo_detail_three/%Y/%m/%d/', blank=True, default='')
    type_of_animal = models.CharField(blank=False, null=False, default='U', max_length=25)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
