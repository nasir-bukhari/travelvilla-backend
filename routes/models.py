from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class JpStopsLahore(models.Model):
    # This field type is a guess.
    geom = models.GeometryField(blank=True, null=True, srid=32643)
    city = models.CharField(max_length=40, blank=True, null=True)
    stop_n = models.CharField(max_length=50, blank=True, null=True)
    point_x = models.FloatField(blank=True, null=True)
    point_y = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jp_stops_lahore'
