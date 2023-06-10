from pytest_factoryboy import register

from tests.factories import UserFactory, AdFactory, CategoryFactory

pytest_plugins = 'tests.fixtures'

register(UserFactory)
register(CategoryFactory)
register(AdFactory)