from .models import Animal
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .pagination import make_pagination

def home_view(request):
    animals = Animal.objects.filter(
        is_staff=True
    ).order_by('-id')


    page_obj, pagination_range = make_pagination(request, animals, 9)

    return render(request, 'dogncat/pages/home.html',
                  context={
                  'animals': page_obj
                  })


def by_animal_type_view(request, type_id):
    animals = get_list_or_404(
        Animal.objects.filter(
            type_of_animal__id=type_id
        ).order_by('-id')
    )
    return render(request, 'dogncat/pages/by_animal_type.html', context={
        'animals' : animals,
    })


def animal(request, id):
    animal = get_object_or_404(Animal, pk=id, is_staff=True,)
    photos = [animal.photo_detail, animal.photo_detail_two, animal.photo_detail_three]
    return render(request, 'dogncat/pages/one_only.html', context={
        'animal': animal,
        'is_detail_page':True,
        'photos':photos,
    })

