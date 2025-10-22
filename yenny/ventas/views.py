from django.shortcuts import render
from .models import Venta

# Create your views here.
def index(request):
    ventas = Venta.objects.all()
    return render(request, 'lista-ventas.html', {'ventas': ventas})
