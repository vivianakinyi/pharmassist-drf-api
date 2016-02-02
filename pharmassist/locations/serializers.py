from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Location


class LocationSerializer(GeoFeatureModelSerializer):

    """A class to serialize locations as GeoJSON compatible data."""

    class Meta:
        model = Location
        geo_field = "point"
