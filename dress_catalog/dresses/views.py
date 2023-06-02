from django.shortcuts import render
from .models import Dress

def dress_list(request):
    dresses = Dress.objects.all()
    return render(request, 'dresses/dress_list.html', {'dresses': dresses})
