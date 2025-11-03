from django.urls import path
from .views import LibroListView, LibroCreateView, LibroUpdateView, LibroDeleteView

urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),
    path('nuevo/', LibroCreateView.as_view(), name='libro-create'),
    path('editar/<int:pk>/', LibroUpdateView.as_view(), name='libro-update'),
    path('eliminar/<int:pk>/', LibroDeleteView.as_view(), name='libro-delete'),
]
