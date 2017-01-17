from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status
from factory.fuzzy import FuzzyInteger


from staff.models import Department
from staff.serializers import DepartmentSerializer
from staff.tests.factories.department import DepartmentFactory
from staff.tests.factories.user import UserFactory
from staff.views import DepartmentViewSet
from staff.tests.support.helpers.views import ViewsHelpers

class DepartmentViewSetSpec(TestCase):

    def setUp(self):
        self.user = ViewsHelpers.force_login_for_views(self.client)
        self.factory = APIRequestFactory()
        self.random_id = FuzzyInteger(1, 10).fuzz()

    def tearDown(self):
        self.user = None
        self.factory = None
        self.random_id = None

    def test_create_department_with_valid_data(self):
        department = DepartmentFactory.stub()
        data = DepartmentSerializer(department).data

        view = DepartmentViewSet.as_view({'post': 'create'})
        url = reverse('department-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get('id'))

    def test_create_department_with_long_name(self):
        department = DepartmentFactory.stub(with_long_name=True)
        data = DepartmentSerializer(department).data

        view = DepartmentViewSet.as_view({'post': 'create'})
        url = reverse('department-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('name'), ['Ensure this field has no more than 250 characters.'])

    def test_create_department_with_duplicated_name(self):
        department_a = DepartmentFactory.create()
        department_b = DepartmentFactory.stub()
        department_b.name = department_a.name
        data = DepartmentSerializer(department_b).data

        view = DepartmentViewSet.as_view({'post': 'create'})
        url = reverse('department-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('name'), ['department with this name already exists.'])

    def test_read_department_fetch_all(self):
        # TODO: assert pagination
        # TODO: assert response schema

        queryset_length = 3
        DepartmentFactory.create_batch(queryset_length)

        view = DepartmentViewSet.as_view({'get': 'list'})
        url = reverse('department-list')
        request = self.factory.get(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_department_when_found(self):
        department = DepartmentFactory.create()

        view = DepartmentViewSet.as_view({'get': 'retrieve'})

        url = reverse('department-detail', args=[department.id])

        request = self.factory.get(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=department.id)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), department.name)

    def test_read_department_when_not_found(self):
        view = DepartmentViewSet.as_view({'get': 'retrieve'})

        url = reverse('department-detail', args=[self.random_id])

        request = self.factory.get(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.random_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_department_when_found(self):
        department = DepartmentFactory.create()

        view = DepartmentViewSet.as_view({'delete': 'destroy'})

        url = reverse('department-detail', args=[department.id])

        request = self.factory.delete(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=department.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_department_when_not_found(self):
        view = DepartmentViewSet.as_view({'delete': 'destroy'})

        url = reverse('department-detail', args=[self.random_id])

        request = self.factory.delete(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.random_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_department_when_not_found(self):
        department = DepartmentFactory.stub()
        data = DepartmentSerializer(department).data

        view = DepartmentViewSet.as_view({'patch': 'partial_update'})

        url = reverse('department-detail', args=[self.random_id])

        request = self.factory.patch(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.random_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_department_when_found(self):
        department_a = DepartmentFactory.create()
        department_b = DepartmentFactory.stub()
        data = DepartmentSerializer(department_b).data

        view = DepartmentViewSet.as_view({'patch': 'partial_update'})
        url = reverse('department-list', args=[department_a.id])
        request = self.factory.patch(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=department_a.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
