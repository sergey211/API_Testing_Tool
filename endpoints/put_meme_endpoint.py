import requests
from endpoints.endpoint_handler import Endpoint


class PutMemeEndpoint(Endpoint):
    token = None
    data = None
    changed_data = None
    # long_url = None
    response = None

    def __init__(self, token, meme_id, data):
        # base_url = self.long_url - WRONG!
        self.data = data
        self.token = token
        self.meme_id = meme_id
        self.changed_data = {
            "id": meme_id,
            "text": "test2",
            "url": "test2",
            "tags": ["test2"],
            "info": {"key3": "key4"}
        }
        self.url = f'http://okulik.site:52355/meme/{self.meme_id}'

    def put_meme(self):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.token }
        changed_data = self.changed_data
        response = requests.put(
            self.url,
            json=changed_data,
            headers=header
        )

        print('code = ', response.status_code)
        print('resp = ', response)
        print('resp.text = ', response.text)
        print('resp.json = ', response.json())
        self.status = response.status_code
        self.response = response.json()

        print(self.response)
        return response
