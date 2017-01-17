from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('name')
    email = factory.Sequence(lambda n: 'test%s@example.com' % n)

    class Meta:
        model = User
