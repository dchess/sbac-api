from rest_framework import serializers
from api.models import Entity, Type


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('url', 'type_id', 'description')


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entity
        fields = (
            'url',
            'county_code',
            'district_code',
            'school_code',
            'test_year',
            'entity_type',
            'county_name',
            'district_name',
            'school_name',
            'zipcode'
        )

