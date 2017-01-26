from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN
from rest_framework.test import APITestCase

from .factories import UserFactory, ProjectFactory, Project
from ..serializers import ProjectSerializer


class ProjectApiTests(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.project = ProjectFactory.build(owner=self.user)
        self.project_data = ProjectSerializer(self.project).data
        self.project_list_url = reverse('project-list')

    def create_project(self):
        self.client.login(username=self.user.username, password=UserFactory.DEFAULT_PASSWORD)
        return self.client.post(self.project_list_url, self.project_data, format='json')

    def test_project_create(self):
        self.assertEqual(Project.objects.count(), 0)
        api_response = self.create_project()
        self.assertEqual(api_response.status_code, HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)

        new_project = Project.objects.get()
        self.assertEqual(new_project.name, self.project_data['name'])
        self.assertEqual(new_project.website, self.project_data['website'])
        self.assertEqual(new_project.description, self.project_data['description'])
        self.assertEqual(new_project.logo, self.project_data['logo'])
        self.assertEqual(new_project.owner, self.user)

    def test_project_create_anon(self):
        api_response = self.client.post(self.project_list_url, self.project_data, format='json')
        self.assertEqual(api_response.status_code, HTTP_403_FORBIDDEN)

    def test_project_list(self):
        api_response = self.client.get(self.project_list_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)

    def test_project_detail(self):
        self.create_project()
        new_project = Project.objects.get()
        api_response = self.client.get(
            reverse('project-detail', kwargs={'pk': new_project.pk})
        )
        self.assertEqual(api_response.status_code, HTTP_200_OK)
        self.assertEqual(api_response.data['name'], self.project_data['name'])
        self.assertEqual(api_response.data['website'], self.project_data['website'])
        self.assertEqual(api_response.data['description'], self.project_data['description'])
        self.assertEqual(api_response.data['logo'], self.project_data['logo'])

