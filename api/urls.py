from django.conf.urls import url, include
from rest_framework import routers

from .views import StationViewSet, MeteringViewSet, ProjectViewSet, schema_view



router = routers.DefaultRouter()
router.register(r'station', StationViewSet)
router.register(r'metering', MeteringViewSet)
router.register(r'project', ProjectViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/docs/',  schema_view),
)
