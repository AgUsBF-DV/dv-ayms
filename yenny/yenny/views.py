
from django.shortcuts import render, redirect
from empleados.forms import LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    if not request.user.is_authenticated:
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
    else:
        return render(request, 'index.html')
