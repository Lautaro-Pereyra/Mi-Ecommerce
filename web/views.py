from rest_framework import generics
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer


# Create your views here.


class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    lookup_url_kwarg = 'producto_id'
    serializer_class = ProductoSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg = 'categoria_id' 
    serializer_class = CategoriaSerializer