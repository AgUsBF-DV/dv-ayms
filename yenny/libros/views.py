from django.shortcuts import render
from .models import Libro

# Create your views here.
def index(request):
    libros = Libro.objects.all()
    return render(request, 'lista-libros.html', {'libros': libros})
