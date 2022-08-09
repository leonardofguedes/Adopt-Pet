from .models import Animal
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_view(request):
    object_list = Animal.objects.filter(
        is_staff=True
    ).order_by('-id')
    paginator = Paginator(object_list, 8)
    page = request.GET.get('page')
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)
    return render(request, 'dogncat/pages/home.html',
                  context={
                  'animals': animals,
                  'page': page,
                  })


def animal(request, id):
    animal = get_object_or_404(Animal, pk=id, is_staff=True,)
    photos = [animal.photo_detail, animal.photo_detail_two, animal.photo_detail_three]
    return render(request, 'dogncat/pages/one_only.html', context={
        'animal': animal,
        'is_detail_page': True,
        'photos': photos,
    })

