import pytest
from endpoints.authorize_endpoint import AuthorizeEndpoint


@pytest.fixture(scope="session")
def token():
    endpoint = AuthorizeEndpoint()
    endpoint.get_token()
    return endpoint.token
