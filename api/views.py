from rest_framework import viewsets
from api.models import Entity, Type
from api.serializers import EntitySerializer, TypeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
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
