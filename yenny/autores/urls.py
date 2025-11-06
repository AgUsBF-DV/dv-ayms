from django.urls import path
from .views import AutorListView, AutorCreateView, AutorUpdateView, AutorDeleteView, AutorShowView

urlpatterns = [
    path('', AutorListView.as_view(), name='autor-list'),
    path('nuevo/', AutorCreateView.as_view(), name='autor-create'),
    path('editar/<int:pk>/', AutorUpdateView.as_view(), name='autor-update'),
    path('eliminar/<int:pk>/', AutorDeleteView.as_view(), name='autor-delete'),
    path('ver/<int:pk>/', AutorShowView.as_view(), name='autor-show'),
]
