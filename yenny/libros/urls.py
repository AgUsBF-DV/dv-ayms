from django.urls import path
from .views import LibroListView

urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),
]
