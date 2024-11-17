from django.urls import path
from . import views

app_name = 'randomizer'

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_groups, name='generate_groups'),
]
