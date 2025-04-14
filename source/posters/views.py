from django.shortcuts import render, redirect
from .models import Poster

# Create your views here.
def view_index(request):
    return render(request, "home.html", context={
        "poster_entries": Poster.objects.all(),
    })