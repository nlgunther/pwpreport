from django.urls import path
from . import views

urlpatterns = [
    path('', views.snpsector, name='snpsector.html'),
]

