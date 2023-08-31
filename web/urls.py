from django.urls import path
from . import views

urlpatterns = [
    path('producto', views.ProductoList.as_view()),
    path('producto/<int:producto_id>', views.ProductoDetail.as_view()),
    path('categoria', views.CategoriaList.as_view()),
    path('categoria/<int:categoria_id>', views.CategoriaDetail.as_view()),
]
