from rest_framework import serializers
from api.models import Entity, Type, Test, Grade, SubGroup


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class SubGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubGroup
        fields = '__all__'
