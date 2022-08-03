from django.urls import path
from .views import home_view, by_animal_type_view, animal

app_name = 'dogncat'

urlpatterns = [
    path('', home_view, name="home"),
    path('animal-type/<int:type_id>/', by_animal_type_view, name="animal-type"),
    path('animal/<int:id>/', animal, name="animal"),
    ]

