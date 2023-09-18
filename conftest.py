import pytest
# import config
from endpoints.authorize_endpoint import AuthorizeEndpoint
from endpoints.post_meme_endpoint import PostMemeEndpoint


@pytest.fixture(scope="session")
def token():
    endpoint = AuthorizeEndpoint()
    endpoint.get_token()
    return endpoint.token


@pytest.fixture(scope="session")
def endpoint(token):
    endpoint = PostMemeEndpoint(token)
    endpoint.post_meme()
    return endpoint

