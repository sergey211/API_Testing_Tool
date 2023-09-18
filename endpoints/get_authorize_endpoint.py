import requests
from endpoints.endpoint_handler import Endpoint


class GetAuthorizeEndpoint(Endpoint):
    token = None
    # user = None
    # long_url = None
    # max_id = None
    # resp_text = None

    def __init__(self, token):
        # base_url = self.long_url - WRONG!
        self.token = token
        self.url = f'http://okulik.site:52355/authorize/{token}'

    def check_token(self):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

        response = requests.get(
            self.url,
            headers=header
        )
        self.status = response.status_code
        print(self.status)
        print(response.text)
        return response.text


