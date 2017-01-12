from rest_framework.filters import FilterSet
from .models import Station, Metering, Project


class StationFilterSet(FilterSet):
    class Meta:
        model = Station
        fields = ['name', 'is_in_test_mode', 'country', 'state', 'county', 'community', 'owner', 'project', 'created',
                  'updated']


class MeteringFilterSet(FilterSet):
    class Meta:
        model = Metering
        fields = ['created', 'station']


class ProjectFilterSet(FilterSet):
    class Meta:
        model = Project
        fields = ['name', 'created', 'updated']
