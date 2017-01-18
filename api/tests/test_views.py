from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.status import HTTP_200_OK

from .factories import ProjectFactory
from api.serializers import ProjectSerializer

import pytest


class ProjectApiTests(APITestCase):

    @pytest.mark.django_db
    def test_project_list(self):
        api_url = reverse('project-list')
        api_response = self.client.get(api_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)
