from unittest import mock
from django.test import TestCase
from django.utils import timezone
from factory.fuzzy import FuzzyText

from staff.models import AbstractBaseModel, Department
from staff.tests.factories.department import DepartmentFactory

FROZEN_DATETIME_NOW = timezone.now()

class AbstractBaseModelSpec(TestCase):

    def frozen_datetime_now():
        return FROZEN_DATETIME_NOW

    def test_created_at_is_automatically_generated(self):
        """
        created_at field is automatically generated at object creation
        """

        department = DepartmentFactory.create()

        self.assertIsNotNone(department.created_at)

    @mock.patch('django.utils.timezone.now', side_effect=frozen_datetime_now)
    def test_created_at_is_equal_to_now(self, *kwargs):
        """
        created_at field generated value must be equal to this moment
        """

        department = DepartmentFactory.create()

        self.assertEqual(department.created_at, FROZEN_DATETIME_NOW)

    def test_created_at_is_not_regenerated_on_updates(self):
        """
        created_at field is not regenerated on updates to object
        """

        department = DepartmentFactory.create()
        first_created_at = department.created_at
        department.name = FuzzyText()
        department.save()

        self.assertEqual(first_created_at, department.created_at)
        self.assertIsNotNone(department.created_at) # just a double-check

    def test_updated_at_is_automatically_generated(self):
        """
        updated_at field is automatically generated at object creation
        """

        department = DepartmentFactory.create()

        self.assertIsNotNone(department.updated_at)

    @mock.patch('django.utils.timezone.now', side_effect=frozen_datetime_now)
    def test_updated_at_is_equal_to_now(self, *kwargs):
        """
        updated_at field generated value must be equal to this moment
        """

        department = DepartmentFactory.create()

        self.assertEqual(department.updated_at, FROZEN_DATETIME_NOW)

    def test_updated_at_is_regenerated_on_updates(self):
        """
        updated_at field is automatically generated on updates to object
        """

        department = DepartmentFactory.create()
        first_updated_at = department.updated_at
        department.name = FuzzyText()
        department.save()

        self.assertNotEqual(first_updated_at, department.updated_at)
        self.assertIsNotNone(department.updated_at) # just a double-check
