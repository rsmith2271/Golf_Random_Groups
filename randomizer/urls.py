from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'randomizer'

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_groups, name='generate_groups'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='randomizer:login'), name='logout'),
]
