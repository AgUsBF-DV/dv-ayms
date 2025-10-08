from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import LoginForm


def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['usernameOrEmail']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username_or_email,
                password=password
            )

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.firstName}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username/email or password.')
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})


def logoutView(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required
def dashboardView(request):
    user = request.user

    admin_cards = [
        {'title': 'Manage Books', 'url': '/books/', 'description': 'Add, edit, and manage book catalog'},
        {'title': 'Manage Authors', 'url': '/authors/', 'description': 'Manage book authors'},
        {'title': 'Manage Categories', 'url': '/categories/', 'description': 'Organize book categories'},
        {'title': 'Manage Publishers', 'url': '/publishers/', 'description': 'Manage publishing companies'},
        {'title': 'Manage Customers', 'url': '/customers/', 'description': 'Customer management'},
        {'title': 'Manage Employees', 'url': '/employees/', 'description': 'Employee administration'},
        {'title': 'Sales Management', 'url': '/sales/', 'description': 'Process and view sales'},
        {'title': 'Reports', 'url': '/reports/', 'description': 'Daily sales reports and analytics'},
        {'title': 'Price Adjustments', 'url': '/price-adjustments/', 'description': 'Bulk price updates'},
    ]

    clerk_cards = [
        {'title': 'View Books', 'url': '/books/', 'description': 'Browse book catalog'},
        {'title': 'Manage Customers', 'url': '/customers/', 'description': 'Customer management'},
        {'title': 'Sales Management', 'url': '/sales/', 'description': 'Process sales'},
    ]

    if user.role.name == 'ADMIN':
        available_cards = admin_cards
        welcome_message = f'Welcome, Administrator {user.firstName}!'
    else:
        available_cards = clerk_cards
        welcome_message = f'Welcome, {user.firstName}!'

    context = {
        'user': user,
        'cards': available_cards,
        'welcome_message': welcome_message,
        'is_admin': user.role.name == 'ADMIN',
    }

    return render(request, 'core/dashboard.html', context)
