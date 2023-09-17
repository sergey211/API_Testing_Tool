from endpoints.delete_meme_endpoint import DeleteMemeEndpoint


def test_delete_meme_by_id(token, endpoint):
    endpoint_meme = DeleteMemeEndpoint(token, endpoint)
    resp_text = endpoint_meme.delete_meme().text
    assert endpoint_meme.status_code_is_200()
    assert "successfully deleted" in resp_text


