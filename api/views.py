from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Entity, Type, Test
from api.serializers import EntitySerializer, TypeSerializer, TestSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = (
        'county_code',
        'district_code',
        'school_code',
        'test_year',
        'entity_type',
        'zipcode',
    )
    search_fields = ('county_name', 'district_name', 'school_name')


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
