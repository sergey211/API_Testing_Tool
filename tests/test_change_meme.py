from endpoints.put_meme_endpoint import PutMemeEndpoint


def test_change_meme_by_id(token, meme_id, data):
    endpoint_meme = PutMemeEndpoint(token, meme_id, data)
    endpoint_meme.put_meme()
    assert endpoint_meme.status_code_is_200()
    assert endpoint_meme.code_is_not_the_same_as_custom()


