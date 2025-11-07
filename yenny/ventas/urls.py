from django.urls import path
from .views import VentaListView, VentaCreateView, VentaUpdateView, VentaDeleteView, VentaShowView

urlpatterns = [
    path('', VentaListView.as_view(), name='venta-list'),
    path('nuevo/', VentaCreateView.as_view(), name='venta-create'),
    path('editar/<int:pk>/', VentaUpdateView.as_view(), name='venta-update'),
    path('eliminar/<int:pk>/', VentaDeleteView.as_view(), name='venta-delete'),
    path('ver/<int:pk>/', VentaShowView.as_view(), name='venta-show'),
]
