from django.urls import path
from .views import HomeView, animal

app_name = 'dogncat'

urlpatterns = [
    #path('', home_view, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('animal/<int:id>/', animal, name="animal")
    ]

