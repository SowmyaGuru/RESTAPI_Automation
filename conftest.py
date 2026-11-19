import pytest
from utils.api_client import APIClient
from utils.auth_helper import AuthHelper

@pytest.fixture
def api_client():

    return APIClient()

@pytest.fixture
def auth_token(api_client):
    auth = AuthHelper(api_client)

    return auth.get_access_token()