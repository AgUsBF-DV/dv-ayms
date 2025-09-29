from django.shortcuts import render
from .models import Editorial

# Create your views here.
def index(request):
    editoriales = Editorial.objects.all()
    return render(request, 'lista-editoriales.html', {'editoriales': editoriales})