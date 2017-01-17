from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from staff.models import Department, AbstractBaseModel
from staff.tests.factories.department import DepartmentFactory

from factory.fuzzy import FuzzyText, FuzzyInteger

class DepartmentSpec(TestCase):

    def setUp(self):
        self.subject = DepartmentFactory.create()

    def terDown(self):
        self.subject = None

    def test_extends_abstract_base_model(self):
        """
        it extends AbstractBaseModel
        """

        self.assertIsInstance(self.subject, AbstractBaseModel)

    def test_str_returns_its_name(self):
        """
        __str__ method returns its name
        """

        self.assertEqual(self.subject.__str__(), self.subject.name)

    def test_name_must_be_unique(self):
        """
        name field must be unique
        """

        name = self.subject.name
        expected_exception_msg = 'UNIQUE constraint failed: staff_department.name'

        with self.assertRaisesRegexp(IntegrityError, expected_exception_msg):
            DepartmentFactory.create(name=name)

    def test_name_cannot_be_blank(self):
        """
        name field cannot be blank
        """

        self.subject.name = ''
        expected_exception_msg = 'name.*This field cannot be blank'

        with self.assertRaisesRegexp(ValidationError, expected_exception_msg):
            self.subject.full_clean()

    def test_name_invalid_with_more_than_250_chars(self):
        """
        name field cannot contain more than 250 characters
        """

        self.subject.name = FuzzyText(length=255).fuzz()
        expected_exception_msg = 'name.*Ensure this value has at most 250 characters'

        with self.assertRaisesRegexp(ValidationError, expected_exception_msg):
            self.subject.full_clean()

    def test_name_valid_with_at_most_250_chars(self):
        """
        name field can contain at most 250 chars
        """

        self.subject.name = FuzzyText(length=FuzzyInteger(1, 10).fuzz()).fuzz()

        self.subject.full_clean()
