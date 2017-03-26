from django.core.cache import cache
from rest_framework import response, schemas
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet
from rest_framework_gis.filters import InBBoxFilter
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from .exceptions import StationWrongToken
from .filters import StationFilterSet, MeteringFilterSet, MeteringHistoryFilterSet, ProjectFilterSet
from .models import Station, Metering, MeteringHistory, Project
from .serializers import StationSerializer, MeteringSerializer, MeteringHistorySerializer, ProjectSerializer


class ObtainJWT(ObtainJSONWebToken):
    authentication_classes = (BasicAuthentication,)


class StationViewSet(ModelViewSet):
    """ViewSet for the Station class"""

    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [InBBoxFilter]
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_class = StationFilterSet
    ordering_fields = ('updated', 'created', 'name')
    bbox_filter_field = 'position'


class MeteringViewSet(ModelViewSet):
    """ViewSet for the Metering class"""

    queryset = Metering.objects.all()
    serializer_class = MeteringSerializer
    filter_class = MeteringFilterSet
    ordering_fields = ('created',)

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            token = data.pop('token')
        except KeyError:
            raise StationWrongToken
        else:
            try:
                station = Station.objects.get(token=token)
            except Station.DoesNotExist:
                raise StationWrongToken
            else:
                data['station'] = station.pk
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                cache.delete(station.last_metering_cache_key)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

    # permission_classes decorator seems not to be working for create, update, list and other base actions
    # http://stackoverflow.com/a/30624527/479931
    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [AllowAny]
        return super(self.__class__, self).get_permissions()


class MeteringHistoryViewSet(ModelViewSet):
    """ViewSet for the MeteringHistory class"""

    queryset = MeteringHistory.objects.all()
    serializer_class = MeteringHistorySerializer
    filter_class = MeteringHistoryFilterSet
    ordering_fields = ('created',)


class ProjectViewSet(ModelViewSet):
    """ViewSet for the Project class"""

    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [InBBoxFilter]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_class = ProjectFilterSet
    ordering_fields = ('updated', 'created', 'name')
    bbox_filter_field = 'position'


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Air Monitor REST API')
    return response.Response(generator.get_schema(request=request))

