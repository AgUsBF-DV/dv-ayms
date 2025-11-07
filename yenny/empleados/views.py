from .forms import EmpleadoForm, LoginForm
from .models import Empleado
from django.contrib.auth import authenticate, login, logout
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'lista-empleados.html'
    paginate_by = 10
    ordering = ['last_name', 'first_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Apellido', 'Email', 'Rol', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for empleado in objeto_pag:
            campos = [
                empleado.id,
                getattr(empleado, 'first_name', ''),
                getattr(empleado, 'last_name', ''),
                getattr(empleado, 'email', ''),
                empleado.get_rol_display(),
                '',  # para la botonera
            ]
            registros.append({'objeto': empleado, 'campos': campos})
        context.update({
            'titulo': 'Lista de Empleados',
            'path_crear': '/empleados/nuevo/',
            'texto_crear': '+ Nuevo Empleado',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
            'modelo': 'empleado',
        })

        if self.request.GET.get('error') == 'protected':
            context['error_message'] = "No se puede eliminar el empleado porque tiene ventas asociadas."
        
        return context

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado-form.html'
    success_url = '/empleados/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.object.email
        self.object.save()
        return super().form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado-form.html'
    success_url = '/empleados/'

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado-confirm-delete.html'
    success_url = '/empleados/'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return redirect(self.success_url + '?error=protected')

# Vista de solo lectura para mostrar un empleado
class EmpleadoShowView(EmpleadoUpdateView):
    template_name = 'empleado-form.html'
    
    # Cargar el formulario en modo solo lectura
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
        return form

    # No permitir POST (no guardar cambios)
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

def logout_view(request):
    logout(request)
    return redirect('empleado-login')

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