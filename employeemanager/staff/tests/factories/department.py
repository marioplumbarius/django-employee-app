import factory

from staff.models import Department


class DepartmentFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = Department

    class Params:
        with_long_name = factory.Trait(
            name=factory.fuzzy.FuzzyText(length=255).fuzz()
        )
