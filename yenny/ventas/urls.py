from django.urls import path
from .views import VentaListView

urlpatterns = [
    path('', VentaListView.as_view(), name='venta-list'),
]
