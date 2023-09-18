import pytest
from endpoints.post_meme_endpoint import PostMemeEndpoint


# @pytest.mark.skip('for testing skipping') # if we skip this test - we getting an error 500
# @pytest.mark.critical
def test_add_new_meme(token):
    endpoint_meme = PostMemeEndpoint(token)
    endpoint_meme.post_meme()
    assert endpoint_meme.status_code_is_200()
    assert endpoint_meme.code_is_the_same_as_custom()


@pytest.mark.skip('for testing skipping')
@pytest.mark.critical
def test_add_new_meme_with_bad_data(token):
    data = {"text": "test", "tags": ["test"], "info": {"key1": "key2"}}
    endpoint_meme = PostMemeEndpoint(token, data)
    endpoint_meme.post_meme()
    assert endpoint_meme.status_code_is_500()

