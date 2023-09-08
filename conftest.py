import pytest
from endpoints.authorize_endpoint import AuthorizeEndpoint


@pytest.fixture()
def new_token():
    url = "http://okulik.site:52355/authorize"
    namee = "Sergey"
    endpoint = AuthorizeEndpoint(url, namee)
    endpoint.get_token()
    return endpoint.token
