from django.urls import path
from .views import EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView

urlpatterns = [
    path('', EmpleadoListView.as_view(), name='empleado-list'),
    path('nuevo/', EmpleadoCreateView.as_view(), name='empleado-create'),
    path('editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado-update'),
    path('eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado-delete'),
]
