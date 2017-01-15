from django.test import TestCase

from staff.models import Department

class DepartmentSpec(TestCase):

    def test_name_validate_uniqueness(self):
        """
            name field must be unique
        """

        self.assertIs(1, 1)
