from django.urls import path
from . import views

app_name = 'my_django_app'

urlpatterns = [
    path('example_vue_app/', views.example_vue_app, name='example_vue_app'),
]
