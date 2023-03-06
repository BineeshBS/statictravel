from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team


# Create your views here.
def home(request):
    obj = place.objects.all()
    obj1 = team.objects.all()

    return render(request, 'home.html', {'result': obj, 'res': obj1})
