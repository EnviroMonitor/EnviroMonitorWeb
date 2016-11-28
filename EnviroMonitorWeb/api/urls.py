from django.conf.urls import url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'station', api.StationViewSet)
router.register(r'metering', api.MeteringViewSet)
router.register(r'project', api.ProjectViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Station
    url(r'^api/station/$', views.StationListView.as_view(), name='api_station_list'),
    url(r'^api/station/create/$', views.StationCreateView.as_view(), name='api_station_create'),
    url(r'^api/station/detail/(?P<id>\S+)/$', views.StationDetailView.as_view(), name='api_station_detail'),
    url(r'^api/station/update/(?P<id>\S+)/$', views.StationUpdateView.as_view(), name='api_station_update'),
)

urlpatterns += (
    # urls for Metering
    url(r'^api/metering/$', views.MeteringListView.as_view(), name='api_metering_list'),
    url(r'^api/metering/create/$', views.MeteringCreateView.as_view(), name='api_metering_create'),
    url(r'^api/metering/detail/(?P<id>\S+)/$', views.MeteringDetailView.as_view(), name='api_metering_detail'),
    url(r'^api/metering/update/(?P<id>\S+)/$', views.MeteringUpdateView.as_view(), name='api_metering_update'),
)

urlpatterns += (
    # urls for Project
    url(r'^api/project/$', views.ProjectListView.as_view(), name='api_project_list'),
    url(r'^api/project/create/$', views.ProjectCreateView.as_view(), name='api_project_create'),
    url(r'^api/project/detail/(?P<slug>\S+)/$', views.ProjectDetailView.as_view(), name='api_project_detail'),
    url(r'^api/project/update/(?P<slug>\S+)/$', views.ProjectUpdateView.as_view(), name='api_project_update'),
)

