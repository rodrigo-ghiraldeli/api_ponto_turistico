from rest_framework.decorators import action
from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class PontoTuristicoViewSet(ModelViewSet):

    # http_method_names = ['DELETE', ]

    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    # query string / forma 1 - queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_fields = ['nome', 'descricao']
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', '^endereco__linha1')

    # alterar a chave de busca, padrão é por ID
    # lookup_field = 'nome'

    def get_queryset(self):

        # query string / forma 2 - return PontoTuristico.objects.filter(aprovado=True)

        # query string / forma 3 - receber os parâmetros
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def teste1(self, request, pk=None):
        pass

    @action(detail=False, methods=['get'])
    def teste2(self, request):
        pass
