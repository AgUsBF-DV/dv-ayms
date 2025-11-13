from django.urls import path
from .views import EditorialListView, EditorialCreateView, EditorialUpdateView, EditorialDeleteView, EditorialShowView

urlpatterns = [
    path('', EditorialListView.as_view(), name='editorial-list'),
    path('nuevo/', EditorialCreateView.as_view(), name='editorial-create'),
    path('editar/<int:pk>/', EditorialUpdateView.as_view(), name='editorial-update'),
    path('eliminar/<int:pk>/', EditorialDeleteView.as_view(), name='editorial-delete'),
    path('ver/<int:pk>/', EditorialShowView.as_view(), name='editorial-show'),
]
