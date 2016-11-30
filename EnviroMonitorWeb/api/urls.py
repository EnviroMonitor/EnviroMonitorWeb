from django.conf.urls import url, include
from rest_framework import routers

from .api import StationViewSet, MeteringViewSet, ProjectViewSet
from .views import StationListView, StationCreateView, StationDetailView, StationUpdateView, MeteringListView, \
    MeteringCreateView, MeteringDetailView, MeteringUpdateView, ProjectListView, ProjectCreateView, ProjectDetailView, \
    ProjectUpdateView

router = routers.DefaultRouter()
router.register(r'station', StationViewSet)
router.register(r'metering', MeteringViewSet)
router.register(r'project', ProjectViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Station
    url(r'^api/station/$', StationListView.as_view(), name='api_station_list'),
    url(r'^api/station/create/$', StationCreateView.as_view(), name='api_station_create'),
    url(r'^api/station/detail/(?P<id>\S+)/$', StationDetailView.as_view(), name='api_station_detail'),
    url(r'^api/station/update/(?P<id>\S+)/$', StationUpdateView.as_view(), name='api_station_update'),
)

urlpatterns += (
    # urls for Metering
    url(r'^api/metering/$', MeteringListView.as_view(), name='api_metering_list'),
    url(r'^api/metering/create/$', MeteringCreateView.as_view(), name='api_metering_create'),
    url(r'^api/metering/detail/(?P<id>\S+)/$', MeteringDetailView.as_view(), name='api_metering_detail'),
    url(r'^api/metering/update/(?P<id>\S+)/$', MeteringUpdateView.as_view(), name='api_metering_update'),
)

urlpatterns += (
    # urls for Project
    url(r'^api/project/$', ProjectListView.as_view(), name='api_project_list'),
    url(r'^api/project/create/$', ProjectCreateView.as_view(), name='api_project_create'),
    url(r'^api/project/detail/(?P<slug>\S+)/$', ProjectDetailView.as_view(), name='api_project_detail'),
    url(r'^api/project/update/(?P<slug>\S+)/$', ProjectUpdateView.as_view(), name='api_project_update'),
)
