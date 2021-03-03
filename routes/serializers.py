from rest_framework import serializers
from .models import JpStopsLahore


class RoutesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JpStopsLahore
        fields = ('id', 'stop_name', 'point_x', 'point_y', 'city_name')
