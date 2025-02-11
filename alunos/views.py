from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Estado, Cidade, Pessoa
from .serializers import EstadoSerializer, CidadeSerializer, PessoaSerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer