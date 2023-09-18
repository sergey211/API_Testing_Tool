from endpoints.get_authorize_endpoint import GetAuthorizeEndpoint


def test_live_token_check(token):
    endpoint_meme = GetAuthorizeEndpoint(token)
    resp_text = endpoint_meme.check_token()
    assert "Token is alive" in resp_text
    assert endpoint_meme.status_code_is_200()


def test_bad_token_check(token):
    endpoint_meme = GetAuthorizeEndpoint("bad_token")
    resp_text = endpoint_meme.check_token()
    assert "Token not found" in resp_text
    assert endpoint_meme.status_code_is_404()