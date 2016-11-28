import models
import serializers
from rest_framework import viewsets, permissions


class StationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Station class"""

    queryset = models.Station.objects.all()
    serializer_class = serializers.StationSerializer
    permission_classes = [permissions.IsAuthenticated]


class MeteringViewSet(viewsets.ModelViewSet):
    """ViewSet for the Metering class"""

    queryset = models.Metering.objects.all()
    serializer_class = serializers.MeteringSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Project class"""

    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


