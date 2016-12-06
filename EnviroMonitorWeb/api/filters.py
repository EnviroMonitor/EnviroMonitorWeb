from rest_framework.filters import FilterSet
from .models import Station, Metering, Project


class StationFilterSet(FilterSet):

    class Meta:
        model = Station
        fields =['name', 'test', 'country', 'state', 'county', 'community', 'owner', 'project']


class MeteringFilterSet(FilterSet):

    class Meta:
        model = Metering
        fields =['created', 'station']


class ProjectFilterSet(FilterSet):

    class Meta:
        model = Project
        fields =['name']
