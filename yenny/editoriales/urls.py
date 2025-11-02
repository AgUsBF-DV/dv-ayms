from django.urls import path
from .views import EditorialListView

urlpatterns = [
    path('', EditorialListView.as_view(), name='editorial-list'),
]
