import requests
from endpoints.endpoint_handler import Endpoint


class PostMemeEndpoint(Endpoint):
    token = None
    data = {
            "text": "test",
            "url": "test",
            "tags": ["test"],
            "info": {"key1": "key2"}
        }
    meme_id = None
    responce = None

    def __init__(self, token):
        # base_url = self.long_url - WRONG!
        self.token = token
        self.url = 'http://okulik.site:52355/meme'

    def post_meme(self):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.token}
        data = self.data
        response = requests.post(
            'http://okulik.site:52355/meme',
            json=data,
            headers=header
        )


        # print(response.status_code)
        self.status = response.status_code
        self.response = response.json()
        print(self.response)
        print('post self.data = ', self.data)
        # print(self.response.text)
        print(response.json()['id'])
        self.meme_id = response.json()['id']
        return response.json()['id']


