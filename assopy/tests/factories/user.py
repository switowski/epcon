import factory
from django_factory_boy import auth as auth_factories


class AssopyUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'assopy.AssopyUser'

    user = factory.SubFactory(auth_factories.UserFactory)
