from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN

from factory import build as factory_build

from .factories import UserFactory, ProjectFactoryForTesting, Project, user_password


class ProjectApiTests(APITestCase):
    def setUp(self):
        self.api_data = factory_build(dict, FACTORY_CLASS=ProjectFactoryForTesting)
        self.api_url = reverse('project-list')
        self.user = UserFactory()

    def test_project_create(self):
        self.client.login(username=self.user.username, password=user_password)
        api_response = self.client.post(self.api_url, self.api_data, format='json')
        self.assertEqual(api_response.status_code, HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.get().name, self.api_data['name'])
        self.assertEqual(Project.objects.get().website, self.api_data['website'])
        self.assertEqual(Project.objects.get().description, self.api_data['description'])
        self.assertEqual(Project.objects.get().logo, self.api_data['logo'])

    def test_project_create_anon(self):
        api_response = self.client.post(self.api_url, self.api_data, format='json')
        self.assertEqual(api_response.status_code, HTTP_403_FORBIDDEN)

    def test_project_list(self):
        api_response = self.client.get(self.api_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)

    def test_message_get(self):
        self.client.login(username=self.user.username, password=user_password)
        api_response = self.client.post(self.api_url, self.api_data, format='json')
        self.assertEqual(api_response.status_code, HTTP_201_CREATED)
        api_response = self.client.get('/api/v1/project/1/')
        self.assertEqual(api_response.status_code, HTTP_200_OK)
        self.assertEqual(api_response.data['name'], self.api_data['name'])
        self.assertEqual(api_response.data['website'], self.api_data['website'])
        self.assertEqual(api_response.data['description'], self.api_data['description'])
        self.assertEqual(api_response.data['logo'], self.api_data['logo'])

