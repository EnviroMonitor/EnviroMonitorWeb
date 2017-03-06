from rest_framework.filters import FilterSet

from .models import Station, Metering, MeteringHistory, Project


class StationFilterSet(FilterSet):
    class Meta:
        model = Station
        fields = {
            'name': ['exact', 'icontains'],
            'is_in_test_mode': ['exact'],
            'country': ['exact', 'icontains'],
            'state': ['exact', 'icontains'],
            'county': ['exact', 'icontains'],
            'community': ['exact', 'icontains'],
            'city': ['exact', 'icontains'],
            'district': ['exact', 'icontains'],
            'owner': ['exact'],
            'project': ['exact'],
            'project__name': ['exact', 'icontains'],
            'created': ['lte', 'gte'],
            'updated': ['lte', 'gte'],
        }


class MeteringFilterSet(FilterSet):
    class Meta:
        model = Metering
        fields = {
            'created': ['lte', 'gte'],
            'station': ['exact'],
        }


class MeteringHistoryFilterSet(FilterSet):
    class Meta:
        model = MeteringHistory
        fields = {
            'created': ['lte', 'gte'],
            'station': ['exact'],
        }


class ProjectFilterSet(FilterSet):
    class Meta:
        model = Project
        fields = {
            'name': ['exact', 'icontains'],
            'country': ['exact', 'icontains'],
            'state': ['exact', 'icontains'],
            'county': ['exact', 'icontains'],
            'community': ['exact', 'icontains'],
            'city': ['exact', 'icontains'],
            'district': ['exact', 'icontains'],
            'owner': ['exact'],
            'created': ['lte', 'gte'],
            'updated': ['lte', 'gte'],
        }
