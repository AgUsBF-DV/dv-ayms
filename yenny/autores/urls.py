from django.urls import path
from .views import AutorListView

urlpatterns = [
    path('', AutorListView.as_view(), name='autor-list'),
]
