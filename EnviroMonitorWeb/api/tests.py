import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Station, Metering, Project
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_station(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["type"] = "type"
    defaults["notes"] = "notes"
    defaults["test"] = "test"
    defaults["position"] = "position"
    defaults["country"] = "country"
    defaults["state"] = "state"
    defaults["county"] = "county"
    defaults["community"] = "community"
    defaults["city"] = "city"
    defaults["district"] = "district"
    defaults.update(**kwargs)
    if "owner" not in defaults:
        defaults["owner"] = create_django_contrib_auth_models_user()
    return Station.objects.create(**defaults)


def create_metering(**kwargs):
    defaults = {}
    defaults["pm01"] = "pm01"
    defaults["pm25"] = "pm25"
    defaults["pm10"] = "pm10"
    defaults["temp_out1"] = "temp_out1"
    defaults["temp_out2"] = "temp_out2"
    defaults["temp_out3"] = "temp_out3"
    defaults["hum_out1"] = "hum_out1"
    defaults["hum_out2"] = "hum_out2"
    defaults["hum_out3"] = "hum_out3"
    defaults["temp_int1"] = "temp_int1"
    defaults["hum_int1"] = "hum_int1"
    defaults["rssi"] = "rssi"
    defaults["bpress_out1"] = "bpress_out1"
    defaults.update(**kwargs)
    if "station" not in defaults:
        defaults["station"] = create_station()
    return Metering.objects.create(**defaults)


def create_project(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["project_website"] = "project_website"
    defaults["description"] = "description"
    defaults["logo"] = "logo"
    defaults.update(**kwargs)
    if "project_admin" not in defaults:
        defaults["project_admin"] = create_django_contrib_auth_models_user()
    return Project.objects.create(**defaults)


class StationViewTest(unittest.TestCase):
    '''
    Tests for Station
    '''
    def setUp(self):
        self.client = Client()

    def test_list_station(self):
        url = reverse('api_station_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_station(self):
        url = reverse('api_station_create')
        data = {
            "name": "name",
            "type": "type",
            "notes": "notes",
            "test": "test",
            "position": "position",
            "country": "country",
            "state": "state",
            "county": "county",
            "community": "community",
            "city": "city",
            "district": "district",
            "owner": create_django_contrib_auth_models_user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_station(self):
        station = create_station()
        url = reverse('api_station_detail', args=[station.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_station(self):
        station = create_station()
        data = {
            "name": "name",
            "type": "type",
            "notes": "notes",
            "test": "test",
            "position": "position",
            "country": "country",
            "state": "state",
            "county": "county",
            "community": "community",
            "city": "city",
            "district": "district",
            "owner": create_django_contrib_auth_models_user().id,
        }
        url = reverse('api_station_update', args=[station.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MeteringViewTest(unittest.TestCase):
    '''
    Tests for Metering
    '''
    def setUp(self):
        self.client = Client()

    def test_list_metering(self):
        url = reverse('api_metering_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_metering(self):
        url = reverse('api_metering_create')
        data = {
            "pm01": "pm01",
            "pm25": "pm25",
            "pm10": "pm10",
            "temp_out1": "temp_out1",
            "temp_out2": "temp_out2",
            "temp_out3": "temp_out3",
            "hum_out1": "hum_out1",
            "hum_out2": "hum_out2",
            "hum_out3": "hum_out3",
            "temp_int1": "temp_int1",
            "hum_int1": "hum_int1",
            "rssi": "rssi",
            "bpress_out1": "bpress_out1",
            "station": create_station().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_metering(self):
        metering = create_metering()
        url = reverse('api_metering_detail', args=[metering.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_metering(self):
        metering = create_metering()
        data = {
            "pm01": "pm01",
            "pm25": "pm25",
            "pm10": "pm10",
            "temp_out1": "temp_out1",
            "temp_out2": "temp_out2",
            "temp_out3": "temp_out3",
            "hum_out1": "hum_out1",
            "hum_out2": "hum_out2",
            "hum_out3": "hum_out3",
            "temp_int1": "temp_int1",
            "hum_int1": "hum_int1",
            "rssi": "rssi",
            "bpress_out1": "bpress_out1",
            "station": create_station().id,
        }
        url = reverse('api_metering_update', args=[metering.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProjectViewTest(unittest.TestCase):
    '''
    Tests for Project
    '''
    def setUp(self):
        self.client = Client()

    def test_list_project(self):
        url = reverse('api_project_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_project(self):
        url = reverse('api_project_create')
        data = {
            "name": "name",
            "project_website": "project_website",
            "description": "description",
            "logo": "logo",
            "project_admin": create_django_contrib_auth_models_user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_project(self):
        project = create_project()
        url = reverse('api_project_detail', args=[project.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_project(self):
        project = create_project()
        data = {
            "name": "name",
            "project_website": "project_website",
            "description": "description",
            "logo": "logo",
            "project_admin": create_django_contrib_auth_models_user().id,
        }
        url = reverse('api_project_update', args=[project.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


