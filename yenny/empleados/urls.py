from django.urls import path
from .views import EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView, login_view, logout_view

urlpatterns = [
    path('', EmpleadoListView.as_view(), name='empleado-list'),
    path('nuevo/', EmpleadoCreateView.as_view(), name='empleado-create'),
    path('editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado-update'),
    path('eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado-delete'),
    path('login/', login_view, name='empleado-login'),
    path('logout/', logout_view, name='empleado-logout'),
]
