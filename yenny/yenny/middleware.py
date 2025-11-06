from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware que redirige a login si el usuario no está autenticado.
    Excluye rutas de login, logout y admin.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Rutas que no requieren autenticación
        allowed_paths = [
            reverse('empleado-login'),
            reverse('empleado-logout'),
            '/admin/',
        ]
        if not request.user.is_authenticated and not any(request.path.startswith(path) for path in allowed_paths):
            return redirect('empleado-login')
        return self.get_response(request)
