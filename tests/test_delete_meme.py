from endpoints.delete_meme_endpoint import DeleteMemeEndpoint
from endpoints.get_meme_endpoint import MemeEndpoint
import pytest


@pytest.mark.critical
@pytest.mark.blocker
def test_delete_meme_by_id(token, endpoint):
    endpoint_meme = DeleteMemeEndpoint(token, endpoint)
    resp_text = endpoint_meme.delete_meme().text
    assert endpoint_meme.status_code_is_200()
    assert "successfully deleted" in resp_text


@pytest.mark.critical
@pytest.mark.fixes
def test_delete_absent_mem(token, endpoint):
    get_endpoint_meme = MemeEndpoint(token)
    max_id = get_endpoint_meme.get_meme_max()
    endpoint_meme = DeleteMemeEndpoint(token, endpoint, max_id + 1)
    resp_text = endpoint_meme.delete_meme().text
    assert endpoint_meme.status_code_is_404()
    assert "Not Found" in resp_text


def test_delete_meme_with_bad_token(endpoint):
    endpoint_meme = DeleteMemeEndpoint('bad_token', endpoint)
    resp_text = endpoint_meme.delete_meme().text
    assert endpoint_meme.status_code_is_401()
    assert "Unauthorized" in resp_text


def test_delete_mem_with_bad_id(token, endpoint):
    endpoint_meme = DeleteMemeEndpoint(token, endpoint, 'bad_id')
    resp_text = endpoint_meme.delete_meme().text
    assert endpoint_meme.status_code_is_404()
    assert "The requested URL was not found on the server" in resp_text


def test_delete_mem_with_not_my_owner(token, endpoint):
    endpoint_meme = DeleteMemeEndpoint(token, endpoint, 1)
    resp_text = endpoint_meme.delete_meme().text
    assert endpoint_meme.status_code_is_400()
    assert "You are not the meme owner" in resp_text
