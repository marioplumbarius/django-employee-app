from django.urls import reverse
from django.test import TestCase
from factory.fuzzy import FuzzyInteger
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework import status

from staff.models import Employee
from staff.serializers import EmployeeSerializer
from staff.tests.factories.employee import EmployeeFactory, DepartmentFactory
from staff.tests.factories.user import UserFactory
from staff.tests.support.helpers.views import ViewsHelpers
from staff.views import EmployeeViewSet


class EmployeeViewSetSpec(TestCase):

    def setUp(self):
        self.user = ViewsHelpers.force_login_for_views(self.client)
        self.factory = APIRequestFactory()
        self.random_id = FuzzyInteger(1, 10).fuzz()

    def tearDown(self):
        self.user = None
        self.factory = None
        self.random_id = None

    def test_create_employee_with_valid_data(self):
        department = DepartmentFactory.create()
        employee = EmployeeFactory.build()
        department_url = reverse('department-detail', args=[department.id])
        data = {
            'name': employee.name,
            'email': employee.email,
            'department': department_url
        }

        view = EmployeeViewSet.as_view({'post': 'create'})
        url = reverse('employee-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get('id'))

    def test_create_employee_with_long_name(self):
        employee = EmployeeFactory.build(with_long_name=True)
        data = EmployeeSerializer(employee).data

        view = EmployeeViewSet.as_view({'post': 'create'})
        url = reverse('employee-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.data.get('name'),
            ['Ensure this field has no more than 250 characters.']
        )

    def test_create_employee_with_duplicated_email(self):
        employee_a = EmployeeFactory.create()
        employee_b = EmployeeFactory.build()
        employee_b.email = employee_a.email
        data = EmployeeSerializer(employee_b).data

        view = EmployeeViewSet.as_view({'post': 'create'})
        url = reverse('employee-list')
        request = self.factory.post(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(
            response.data.get('email'),
            ['employee with this email already exists.']
        )

    def test_read_employee_fetch_all(self):
        # TODO: assert pagination
        # TODO: assert response schema

        queryset_length = 3
        EmployeeFactory.create_batch(queryset_length)

        view = EmployeeViewSet.as_view({'get': 'list'})
        url = reverse('employee-list')
        request = self.factory.get(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_employee_when_found(self):
        employee = EmployeeFactory.create()

        view = EmployeeViewSet.as_view({'get': 'retrieve'})

        url = reverse('employee-detail', args=[employee.id])

        request = self.factory.get(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=employee.id)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), employee.name)

    def test_read_employee_when_not_found(self):
        view = EmployeeViewSet.as_view({'get': 'retrieve'})

        url = reverse('employee-detail', args=[self.random_id])

        request = self.factory.get(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.random_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_employee_when_found(self):
        employee = EmployeeFactory.create()

        view = EmployeeViewSet.as_view({'delete': 'destroy'})

        url = reverse('employee-detail', args=[employee.id])

        request = self.factory.delete(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=employee.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_employee_when_not_found(self):
        view = EmployeeViewSet.as_view({'delete': 'destroy'})

        url = reverse('employee-detail', args=[self.random_id])

        request = self.factory.delete(url, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.random_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_employee_when_not_found(self):
        employee = EmployeeFactory.build()
        data = EmployeeSerializer(employee).data

        view = EmployeeViewSet.as_view({'patch': 'partial_update'})

        url = reverse('employee-detail', args=[self.random_id])

        request = self.factory.patch(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.random_id)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_employee_when_found(self):
        employee_a = EmployeeFactory.create()
        employee_b = EmployeeFactory.build()
        department_url = reverse(
            'department-detail',
            args=[employee_a.department.id]
        )
        data = {
            'name': employee_b.name,
            'email': employee_b.email,
            'department': department_url
        }

        view = EmployeeViewSet.as_view({'patch': 'partial_update'})
        url = reverse('employee-list', args=[employee_a.id])
        request = self.factory.patch(url, data, format='json')
        force_authenticate(request, user=self.user)
        response = view(request, pk=employee_a.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
