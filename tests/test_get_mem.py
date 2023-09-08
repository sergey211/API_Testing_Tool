import requests
from endpoints.authorize_endpoint import AuthorizeEndpoint


def test_get_mem():
    url = "http://okulik.site:52355/authorize"
    name = "Sergey"
    endpoint = AuthorizeEndpoint(url, name)
    token = endpoint.get_token()
    print('token=' + token)
    base_url = 'http://okulik.site:52355/meme'
    header = {
        'Content-Type': 'application/json',
        'Authorization': token

    }


    response = requests.get(
        base_url,
        headers=header
    )
    # p_code = response.json()['token']  # HI1qlEj0Z7kIKSA
    print(response.json())
    assert response.status_code == 200
    # assert response.json()['user'] == 'Sergey'
    assert len(response.json()) > 0


def test_not_authorized():
    # token = endp.AuthorizeEndpoint.get_token()
    # print('token='+token)
    base_url = 'http://okulik.site:52355/meme'
    header = {
        'Content-Type': 'application/json',
        'Authorization': 'wrong_token',
    }
    data = {
    }
    response = requests.get(
        base_url,
        headers=header
    )

    assert response.status_code == 401
