from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import EmpleadoForm
from .models import Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'lista-empleados.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Apellido', 'Email', 'Rol', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for empleado in objeto_pag:
            registros.append([
                empleado.id,
                getattr(empleado, 'first_name', ''),
                getattr(empleado, 'last_name', ''),
                getattr(empleado, 'email', ''),
                empleado.get_rol_display(),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Empleados',
            'path_crear': '/empleados/nuevo/',
            'texto_crear': '+ Nuevo Empleado',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado-form.html'
    success_url = '/empleados/'

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado-form.html'
    success_url = '/empleados/'

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado-confirm-delete.html'
    success_url = '/empleados/'

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('empleado-login')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})