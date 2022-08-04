from django.contrib import admin
from .models import Animal, Photo


class PhotoAdmin(admin.StackedInline):
    model = Photo

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Animal


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    ...




