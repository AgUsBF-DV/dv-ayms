from django.shortcuts import redirect
from django.urls import reverse
from urllib import request

class LoginRequiredMiddleware:
    """
    Middleware que redirige a login si el usuario no está autenticado.
    Excluye rutas de login, logout y admin.
    También restringe acceso a rutas de admin para roles específicos.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Rutas que no requieren autenticación
        allowed_paths = [
            reverse("empleado-login"),
            reverse("empleado-logout"),
            # '/admin/',
        ]

        if not request.user.is_authenticated and not any(
            request.path.startswith(path) for path in allowed_paths
        ):
            return redirect("empleado-login")

        # Rutas que requieren rol ADMIN o ENCARGADO
        admin_encargado_paths = [
            "/autores/eliminar/",
            "/libros/eliminar/",
            "/clientes/eliminar/",
            "/ventas/editar/",
            "/categorias/",
            "/editoriales/",
            "/empleados/",
        ]

        if (
            request.user.is_authenticated
            and any(request.path.startswith(path) for path in admin_encargado_paths)
            and request.path != "/empleados/logout/"
        ):
            if request.user.rol not in ["ADMIN", "ENCARGADO"]:
                return redirect("/")  # Redirigir al inicio

        # Rutas que requieren rol ADMIN exclusivamente
        admin_paths = [
            "/ventas/eliminar/",
            "/categorias/eliminar/",
            "/editoriales/eliminar/",
            "/empleados/editar/",
            "/empleados/eliminar/",
        ]

        if request.user.is_authenticated and any(
            request.path.startswith(path) for path in admin_paths
        ):
            if request.user.rol != "ADMIN":
                return redirect("/")  # Redirigir al inicio

        return self.get_response(request)
