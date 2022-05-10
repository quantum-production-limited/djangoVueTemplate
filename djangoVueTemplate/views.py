from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return HttpResponseRedirect(reverse('my_django_app:example_vue_app'))
