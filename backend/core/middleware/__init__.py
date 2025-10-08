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
        # Paths that don't require authentication
        self.public_paths = ["/login/", "/admin/login/"]
        # Get admin-only paths from settings
        self.admin_paths = getattr(settings, 'RBAC_ADMIN_PATHS', [])

    def __call__(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            # Allow access to public paths and static files
            if (request.path in self.public_paths or
                request.path.startswith('/static/') or
                request.path.startswith('/media/') or
                request.path.startswith('/admin/')):
                return self.get_response(request)

            # Redirect unauthenticated users to login
            return redirect(settings.LOGIN_URL)

        # User is authenticated - check role-based permissions
        if hasattr(request.user, 'role') and request.user.role:
            user_role = request.user.role.name

            # CLERK users have restricted access
            if user_role == 'CLERK':
                # Check if trying to access admin-only paths
                for admin_path in self.admin_paths:
                    if request.path.startswith(admin_path):
                        messages.error(
                            request,
                            f'Access denied. You do not have permission to access {request.path}.'
                        )
                        return redirect('dashboard')

        # Allow access for ADMIN users and valid CLERK requests
        return self.get_response(request)
