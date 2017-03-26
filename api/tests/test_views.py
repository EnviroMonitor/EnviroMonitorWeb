from django.contrib.gis.geos.point import Point
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_403_FORBIDDEN
)
from rest_framework.test import APITestCase

from .factories import (
    Project,
    Station,
    ProjectFactory,
    UserFactory,
    StationFactory,
    MeteringFactory
)
from ..serializers import ProjectSerializer, StationSerializer, MeteringSerializer


class UserAuthBase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.jwt_url = reverse('api-token-auth')
        self.user_data = {
            'username': self.user.username,
            'password': UserFactory.DEFAULT_PASSWORD
        }

    def obtain_token_and_set_auth(self):
        response = self.client.post(self.jwt_url, self.user_data)
        return self.client.credentials(HTTP_AUTHORIZATION='JWT ' + response.data['token'])


class ProjectApiTests(UserAuthBase):
    def setUp(self):
        self.project = ProjectFactory.build()
        self.project_data = ProjectSerializer(self.project).data
        self.project_list_url = reverse('project-list')
        return super(ProjectApiTests, self).setUp()

    def create_project(self):
        self.obtain_token_and_set_auth()
        return self.client.post(self.project_list_url, self.project_data)

    def assertProjectDataEqual(self, data):
        self.assertEqual(data['name'], self.project_data['name'])
        self.assertEqual(data['website'], self.project_data['website'])
        self.assertEqual(data['description'], self.project_data['description'])
        self.assertEqual(data['logo'], self.project_data['logo'])
        self.assertEqual(data['position'], self.project_data['position'])
        self.assertEqual(data['country'], self.project_data['country'])
        self.assertEqual(data['state'], self.project_data['state'])
        self.assertEqual(data['county'], self.project_data['county'])
        self.assertEqual(data['community'], self.project_data['community'])
        self.assertEqual(data['city'], self.project_data['city'])
        self.assertEqual(data['district'], self.project_data['district'])

    def test_project_create(self):
        self.assertEqual(Project.objects.count(), 0)
        api_response = self.create_project()
        self.assertEqual(api_response.status_code, HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)

        created_project = Project.objects.get()
        created_project_data = ProjectSerializer(created_project).data
        self.assertProjectDataEqual(created_project_data)
        self.assertEqual(created_project.owner, self.user)

    def test_project_create_anon(self):
        api_response = self.client.post(self.project_list_url, self.project_data)
        self.assertEqual(api_response.status_code, HTTP_401_UNAUTHORIZED)

    def test_project_list(self):
        api_response = self.client.get(self.project_list_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)

    def test_project_detail(self):
        self.create_project()
        created_project = Project.objects.get()
        api_response = self.client.get(
            reverse('project-detail', kwargs={'pk': created_project.pk}),
            format='json'
        )
        self.assertEqual(api_response.status_code, HTTP_200_OK)
        self.assertProjectDataEqual(api_response.data)

    def test_project_detail_id_does_not_exist(self):
        api_response = self.client.get(
            reverse('project-detail', kwargs={'pk': 0}),
            format='json'
        )
        self.assertEqual(api_response.status_code, HTTP_404_NOT_FOUND)

    def test_project_detail_patch(self):
        self.create_project()
        created_project = Project.objects.get()
        api_response = self.client.patch(
            reverse('project-detail', kwargs={'pk': created_project.pk}),
            {'name': 'new_name'},
            format='json'
        )
        self.assertEqual(api_response.status_code, HTTP_200_OK)
        self.assertEqual(api_response.data['name'], 'new_name')

    def test_project_detail_delete(self):
        self.create_project()
        created_project = Project.objects.get()
        api_response = self.client.delete(
            reverse('project-detail', kwargs={'pk': created_project.pk}),
            format='json'
        )
        self.assertEqual(api_response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)

    def test_list_view_filter_in_bbox(self):
        ProjectFactory.create(position=Point([20, 50]))
        ProjectFactory.create(position=Point([21, 51]))
        ProjectFactory.create(position=Point([0, 0]))

        api_response = self.client.get(
            self.project_list_url,
            data={
                'in_bbox': '19, 49, 22, 52'
            }
        )
        self.assertEqual(2, len(api_response.data['results']))

    def test_list_view_filter_owner(self):
        owner = UserFactory()
        ProjectFactory.create(owner=owner)
        ProjectFactory.create(owner=owner)
        ProjectFactory.create()

        api_response = self.client.get(
            self.project_list_url,
            data={
                'owner': owner.pk
            }
        )
        self.assertEqual(2, len(api_response.data['results']))

    def test_list_view_filter_country(self):
        country = 'Poland'
        ProjectFactory.create(country=country)
        ProjectFactory.create(country=country)
        ProjectFactory.create(country='Germany')

        api_response = self.client.get(
            self.project_list_url,
            data={
                'country': country
            }
        )
        self.assertEqual(2, len(api_response.data['results']))

    def test_list_view_filter_country_icontains(self):
        country = 'Poland'
        ProjectFactory.create(country=country)
        ProjectFactory.create(country=country)
        ProjectFactory.create(country='Germany')

        api_response = self.client.get(
            self.project_list_url,
            data={
                'country__icontains': 'pol'
            }
        )
        self.assertEqual(2, len(api_response.data['results']))


class StationApiTests(UserAuthBase):
    def setUp(self):
        self.existing_project = ProjectFactory.create()
        self.station = StationFactory.build(project=self.existing_project)
        self.station_data = StationSerializer(self.station).data
        self.station_list_url = reverse('station-list')
        return super(StationApiTests, self).setUp()

    def create_station(self):
        self.obtain_token_and_set_auth()
        return self.client.post(self.station_list_url, self.station_data)

    def assertStationDataEqual(self, data):
        self.assertEqual(data['name'], self.station_data['name'])
        self.assertEqual(data['type'], self.station_data['type'])
        self.assertEqual(data['notes'], self.station_data['notes'])
        self.assertEqual(data['is_in_test_mode'], self.station_data['is_in_test_mode'])
        self.assertEqual(data['altitude'], self.station_data['altitude'])
        self.assertEqual(data['position'], self.station_data['position'])
        self.assertEqual(data['country'], self.station_data['country'])
        self.assertEqual(data['state'], self.station_data['state'])
        self.assertEqual(data['county'], self.station_data['county'])
        self.assertEqual(data['community'], self.station_data['community'])
        self.assertEqual(data['city'], self.station_data['city'])
        self.assertEqual(data['district'], self.station_data['district'])
        self.assertEqual(data['project'], self.station_data['project'])
        self.assertEqual(data['last_metering'], self.station_data['last_metering'])

    def test_station_create(self):
        self.assertEqual(Station.objects.count(), 0)
        api_response = self.create_station()
        self.assertEqual(api_response.status_code, HTTP_201_CREATED)
        self.assertEqual(Station.objects.count(), 1)

        created_station = Station.objects.get()
        created_station_data = StationSerializer(created_station).data
        self.assertStationDataEqual(created_station_data)
        self.assertEqual(created_station.owner, self.user)

    def test_list_view_filter_in_bbox(self):
        StationFactory.create(position=Point([20, 50]))
        StationFactory.create(position=Point([21, 51]))
        StationFactory.create(position=Point([0, 0]))

        api_response = self.client.get(
            self.station_list_url,
            data={
                'in_bbox': '19, 49, 22, 52'
            }
        )
        self.assertEqual(2, len(api_response.data['results']))


class MeteringApiTests(UserAuthBase):
    def setUp(self):
        self.existing_project = ProjectFactory.create()
        self.existing_station = StationFactory.create(project=self.existing_project)
        self.metering = MeteringFactory.build(station=self.existing_station)
        self.metering_data = MeteringSerializer(self.metering).data
        self.metering_list_url = reverse('metering-list')
        return super(MeteringApiTests, self).setUp()

    def test_add_metering(self):
        # test cache key removal before add_metering
        self.assertEqual(self.existing_station.last_metering, MeteringSerializer(None).data)
        self.assertEqual(self.existing_station.metering_set.count(), 0)

        metering_data = self.metering_data.copy()
        metering_data['token'] = self.existing_station.token
        api_response = self.client.post(self.metering_list_url, metering_data)

        self.assertEqual(api_response.status_code, HTTP_201_CREATED)
        self.assertEqual(self.existing_station.metering_set.count(), 1)

        # test cache key removal after add_metering
        self.assertEqual(
            self.existing_station.last_metering,
            MeteringSerializer(self.existing_station.metering_set.first()).data
        )

    def test_add_metering_no_token(self):
        api_response = self.client.post(self.metering_list_url, {})
        self.assertEqual(api_response.status_code, HTTP_403_FORBIDDEN)

    def test_add_metering_wrong_token(self):
        api_response = self.client.post(self.metering_list_url, {'token': 'xyz'})
        self.assertEqual(api_response.status_code, HTTP_403_FORBIDDEN)

    def test_add_metering_wrong_data(self):
        api_response = self.client.post(self.metering_list_url, {'token': self.existing_station.token})
        self.assertEqual(api_response.status_code, HTTP_400_BAD_REQUEST)
