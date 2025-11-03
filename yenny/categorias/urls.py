from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView

urlpatterns = [
    path('', CategoriaListView.as_view(), name='categoria-list'),
    path('nuevo/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria-update'),
    path('eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria-delete'),
]
