from django.urls import path
from .views import EmpleadoListView

urlpatterns = [
    path('', EmpleadoListView.as_view(), name='empleado-list'),
]
