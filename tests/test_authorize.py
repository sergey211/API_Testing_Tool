import requests
from endpoints.authorize_endpoint import AuthorizeEndpoint


def test_get_token():
    endpoint = AuthorizeEndpoint()
    endpoint.get_token()
    assert endpoint.status_code_is_200()
    assert endpoint.name_of_user_the_same_as_sent()
    assert endpoint.token_is_not_empty()

