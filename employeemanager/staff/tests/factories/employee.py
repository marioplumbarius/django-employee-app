import factory
from factory.fuzzy import FuzzyText

from staff.models import Employee
from staff.tests.factories.department import DepartmentFactory


class EmployeeFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    email = factory.Sequence(
        lambda n: '{0}_{1}@example.com'.format(n, FuzzyText().fuzz()))
    department = factory.SubFactory(DepartmentFactory)

    class Meta:
        model = Employee

    class Params:
        with_long_name = factory.Trait(
            name=factory.fuzzy.FuzzyText(length=255).fuzz()
        )
