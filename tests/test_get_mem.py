from endpoints.meme_endpoint import MemeEndpoint


def test_get_max_mem_id(token):
    endpoint_meme = MemeEndpoint(token)
    endpoint_meme.get_meme_max()
    assert endpoint_meme.status_code_is_200()


def test_not_authorized():
    token = 'WRONG_TOKEN'
    endpoint_meme = MemeEndpoint(token)
    resp_text = endpoint_meme.get_meme_unauth()
    assert "Unauthorized" in resp_text
    assert endpoint_meme.status_code_is_401()


def test_open_mem_by_id(token):
    endpoint_meme = MemeEndpoint(token)
    max_id = endpoint_meme.get_meme_max()
    endpoint_meme = MemeEndpoint(token)
    endpoint_meme.get_mem_by_id(max_id)
    assert endpoint_meme.status_code_is_200()


def test_open_absent_mem(token):
    endpoint_meme = MemeEndpoint(token)
    absent_id = endpoint_meme.get_meme_max() + 1
    endpoint_meme = MemeEndpoint(token)
    resp_text = endpoint_meme.get_mem_by_id(absent_id)
    assert "Not Found" in resp_text
    assert endpoint_meme.status_code_is_404()
