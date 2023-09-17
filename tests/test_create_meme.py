from endpoints.post_meme_endpoint import PostMemeEndpoint


def test_add_new_meme(token):
    endpoint_meme = PostMemeEndpoint(token)
    endpoint_meme.post_meme()
    assert endpoint_meme.status_code_is_200()
    assert endpoint_meme.code_is_the_same_as_custom()



