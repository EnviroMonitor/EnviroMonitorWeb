from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from .models import Station, Metering, Project
from .serializers import StationSerializer, MeteringSerializer, ProjectSerializer
from .filters import StationFilterSet, MeteringFilterSet, ProjectFilterSet


class StationViewSet(ModelViewSet):
    """ViewSet for the Station class"""

    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_class = StationFilterSet


class MeteringViewSet(ModelViewSet):
    """ViewSet for the Metering class"""

    queryset = Metering.objects.all()
    serializer_class = MeteringSerializer
    filter_class = MeteringFilterSet


class ProjectViewSet(ModelViewSet):
    """ViewSet for the Project class"""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_class = ProjectFilterSet


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Air Monitor REST API')
    return response.Response(generator.get_schema(request=request))

