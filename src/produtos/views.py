from rest_framework import status, filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Produto, Estabelecimento
from .serializers import ProdutoSerializer, EstabelecimentoSerializer


class ProductList(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['desc']

class EstablishmentList(generics.ListCreateAPIView):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer
    filterset_fields = ['nm_fan', 'nm_emp', 'bairro', 'mun']
