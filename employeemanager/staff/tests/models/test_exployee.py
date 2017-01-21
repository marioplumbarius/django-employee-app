import random

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from factory.fuzzy import FuzzyText, FuzzyInteger

from staff.models import Employee, AbstractBaseModel
from staff.tests.factories.employee import EmployeeFactory
from staff.tests.factories.department import DepartmentFactory


class EmployeeSpec(TestCase):

    def setUp(self):
        self.subject = EmployeeFactory.create()

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

    def test_name_can_be_duplicated(self):
        """
        name field can be duplicated across different objects
        """

        employee = EmployeeFactory.create()
        employee.name = self.subject.name

        employee.full_clean()

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

    def test_email_must_be_unique(self):
        """
        email field must be unique
        """

        exception_a = 'UNIQUE constraint failed: staff_employee.email'
        exception_b = 'column email is not unique'
        expected_exception_msg = '({0}|{1})'.format(exception_a, exception_b)

        with self.assertRaisesRegexp(IntegrityError, expected_exception_msg):
            EmployeeFactory.create(email=self.subject.email).full_clean()

    def test_department_cannot_be_none(self):
        """
        department field cannot be none
        """

        self.subject.department = None
        expected_exception_msg = 'department.*This field cannot be null'

        with self.assertRaisesRegexp(ValidationError, expected_exception_msg):
            self.subject.full_clean()

    def test_department_must_be_a_saved_instance(self):
        """
        department field must be a saved instance
        """

        self.subject.department = DepartmentFactory.build()
        expected_exception_msg = 'department.*This field cannot be null'

        with self.assertRaisesRegexp(ValidationError, expected_exception_msg):
            self.subject.full_clean()
