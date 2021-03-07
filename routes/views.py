from django.contrib.gis.geos import Point
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import JpStopsLahore
from .serializers import RoutesSerializer

from django.contrib.gis.db.models.functions import Distance
from django.http import JsonResponse


# Create your views here.

class RoutesViewSet(viewsets.ModelViewSet):
    queryset = JpStopsLahore.objects.all().order_by('id')
    serializer_class = RoutesSerializer


@csrf_exempt
def find_nearest_station(request):
    # request.body
    lat = request.GET["lat"]
    long = request.GET["lon"]
    stop_names = []

    point = Point(float(long), float(lat))
    point.srid = 4326
    point.transform(32643)
    qs = JpStopsLahore.objects.all().annotate(distance=Distance("geom", point)).order_by("distance")[:5]
    for obj in qs:
        geom_4326 = obj.geom.transform(4326, True)
        stop_names.append({
            "Stop Name" : obj.stop_n,
            "Longitude" : geom_4326.x,
            "Latitude" : geom_4326.y
        })

    return JsonResponse({'bus_stops': stop_names})
