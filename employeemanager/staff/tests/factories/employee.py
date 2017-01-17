import factory
from factory.fuzzy import FuzzyText

from staff.models import Employee
from staff.tests.factories.department import DepartmentFactory

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    name = factory.Faker('name')
    email = factory.Sequence(lambda n: '{0}_{1}@example.com'.format(n, FuzzyText().fuzz()))
    department = factory.SubFactory(DepartmentFactory)
