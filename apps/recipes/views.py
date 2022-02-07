from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    a = 10
    bb = 'teste agoraa'
    return render(request, 'recipes/index.html', {'a': 'a', 'teste': bb})