from django.contrib.gis.db import models

class Location(models.Model):
    point = models.PointField(srid=4326)  # SRID for WGS 84 (Geographic coordinates)
