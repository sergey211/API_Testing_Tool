import requests
from endpoints.authorize_endpoint import AuthorizeEndpoint
from endpoints.meme_endpoint import MemeEndpoint


def test_get_max_mem_id(new_token):
    token = new_token
    base_url = 'http://okulik.site:52355/meme'
    endpoint_meme = MemeEndpoint(base_url, token)
    endpoint_meme.get_meme_max()
    assert endpoint_meme.status_code_is_200()


def test_not_authorized():
    base_url = 'http://okulik.site:52355/meme'
    token = 'WRONG_TOKEN'
    endpoint_meme = MemeEndpoint(base_url, token)
    endpoint_meme.get_meme_unauth()
    assert endpoint_meme.status_code_is_401()


def test_open_mem_by_id(new_token):
    token = new_token
    base_url = 'http://okulik.site:52355/meme'
    endpoint_meme = MemeEndpoint(base_url, token)
    max_id = endpoint_meme.get_meme_max()
    url_with_id = f'http://okulik.site:52355/meme/{max_id}'
    endpoint_meme = MemeEndpoint(url_with_id, token)
    endpoint_meme.get_mem_by_id()
    assert endpoint_meme.status_code_is_200()


def test_open_absent_mem(new_token):
    token = new_token
    base_url = 'http://okulik.site:52355/meme'
    endpoint_meme = MemeEndpoint(base_url, token)
    max_id = endpoint_meme.get_meme_max() + 1
    url_with_id = f'http://okulik.site:52355/meme/{max_id}'
    endpoint_meme = MemeEndpoint(url_with_id, token)
    endpoint_meme.get_mem_by_id()
    assert endpoint_meme.status_code_is_404()
