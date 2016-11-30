from .models import Station, Metering, Project
from .serializers import StationSerializer, MeteringSerializer, ProjectSerializer
from rest_framework.viewsets import ModelViewSet


class StationViewSet(ModelViewSet):
    """ViewSet for the Station class"""

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class MeteringViewSet(ModelViewSet):
    """ViewSet for the Metering class"""

    queryset = Metering.objects.all()
    serializer_class = MeteringSerializer


class ProjectViewSet(ModelViewSet):
    """ViewSet for the Project class"""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
