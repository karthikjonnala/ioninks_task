from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<slug>', views.movie_detail, name='detail'),
    path('create/', views.movie_create, name='create')
]
