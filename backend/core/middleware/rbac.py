from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from django.urls import reverse


class RBACMiddleware:
    """
    Role-Based Access Control middleware.

    Handles authentication and authorization based on user roles:
    - Redirects unauthenticated users to login (except for login pages and static files)
    - Restricts CLERK users from accessing admin-only paths
    - Allows full access for ADMIN users
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.public_paths = ["/login/", "/admin/login/"]
        self.admin_paths = getattr(settings, 'RBAC_ADMIN_PATHS', [])

    def __call__(self, request):
        if not request.user.is_authenticated:
            if (request.path in self.public_paths or
                request.path.startswith('/static/') or
                request.path.startswith('/media/') or
                request.path.startswith('/admin/')):
                return self.get_response(request)

            return redirect(settings.LOGIN_URL)

        if hasattr(request.user, 'role') and request.user.role:
            user_role = request.user.role.name

            if user_role == 'CLERK':
                for admin_path in self.admin_paths:
                    if request.path.startswith(admin_path):
                        messages.error(
                            request,
                            f'Access denied. You do not have permission to access {request.path}.'
                        )
                        return redirect('dashboard')

        return self.get_response(request)
