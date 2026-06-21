import pytest
from api.endpoints import UserEndpoints, PostEndpoints


@pytest.fixture(scope="session")
def user_client():
    return UserEndpoints()


@pytest.fixture(scope="session")
def post_client():
    return PostEndpoints()