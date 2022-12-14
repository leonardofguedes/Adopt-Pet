from django.urls import path
from users.views import *


urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
    path('newpet/', newpet, name='newpet'),
    path('delete/<int:id>/', dashboard_delete, name='dashboard_delete'),
]