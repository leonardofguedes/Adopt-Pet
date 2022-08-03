from django.contrib import admin
from .models import Type_of_animal, Animal, Photo


class PhotoAdmin(admin.StackedInline):
    model = Photo

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Animal

@admin.register(Type_of_animal)
class Type_of_Animal_Admin(admin.ModelAdmin):
    model = Type_of_animal

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ...




