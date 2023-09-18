import requests
from endpoints.endpoint_handler import Endpoint


class DeleteMemeEndpoint(Endpoint):
    token = None
    # data = None
    # changed_data = None
    # endpoint = None
    # long_url = None
    response = None

    def __init__(self, token, endpoint, meme_id=None):
        # base_url = self.long_url - WRONG!
        # self.data = endpoint.data
        self.token = token
        if meme_id is None:
            self.meme_id = endpoint.meme_id
        else:
            self.meme_id = meme_id
        # self.meme_id = meme_id
        self.changed_data = {
            "id": self.meme_id,
            # "text": "test2",
            # "url": "test2",
            # "tags": ["test2"],
            # "info": {"key3": "key4"}
        }
        self.url = f'http://okulik.site:52355/meme/{self.meme_id}'

    def delete_meme(self):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.token }
        changed_data = self.changed_data
        response = requests.delete(
            self.url,
            json=changed_data,
            headers=header
        )

        print(response.status_code)
        print('code = ', response.status_code)
        print('resp = ', response)
        print('resp.text = ', response.text)
        # print('resp.json = ', response.json()) #

        self.status = response.status_code  # this gives an 400 error (if disabled)
        # self.response = response.json() # give much errors if enabled

        # print(self.response)
        return response
