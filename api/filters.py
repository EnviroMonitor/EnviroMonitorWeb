from rest_framework.filters import FilterSet

from .models import Station, Metering, MeteringHistory, Project


class StationFilterSet(FilterSet):
    class Meta:
        model = Station
        fields = {
            'name': ['icontains'],
            'is_in_test_mode': ['exact'],
            'country': ['icontains'],
            'state': ['icontains'],
            'county': ['icontains'],
            'community': ['icontains'],
            'city': ['icontains'],
            'district': ['icontains'],
            'owner': ['exact'],
            'project': ['exact'],
            'project__name': ['icontains'],
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
            'name': ['icontains'],
            'country': ['icontains'],
            'state': ['icontains'],
            'county': ['icontains'],
            'community': ['icontains'],
            'city': ['icontains'],
            'district': ['icontains'],
            'owner': ['exact'],
            'created': ['lte', 'gte'],
            'updated': ['lte', 'gte'],
        }
