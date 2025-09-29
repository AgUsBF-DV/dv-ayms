from django.shortcuts import render
from .models import Autor

# Create your views here.
def index(request):
    autores = Autor.objects.all()
    return render(request, 'index.html', {'autores': autores})