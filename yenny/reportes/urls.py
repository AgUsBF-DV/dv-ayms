from django.urls import path
from .views import (
    VentasDiariasView,
    RankingLibrosView,
    RankingAutoresView,
    RankingCategoriasView
)

app_name = 'reportes'

urlpatterns = [
    path('ventas-diarias/', VentasDiariasView.as_view(), name='ventas-diarias'),
    path('ranking-libros/', RankingLibrosView.as_view(), name='ranking-libros'),
    path('ranking-autores/', RankingAutoresView.as_view(), name='ranking-autores'),
    path('ranking-categorias/', RankingCategoriasView.as_view(), name='ranking-categorias'),
]
