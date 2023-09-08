import requests


class AuthorizeEndpoint:
    token = None
    status = None
    user = None
    long_url = None

    def __init__(self, long_url, name):
        # base_url = self.long_url - WRONG!
        self.name = name
        self.long_url = long_url

    def get_token(self):

        header = {
            'Content-Type': 'application/json',
        }
        base_url = self.long_url

        data = {
            "name": self.name
        }
        response = requests.post(
            base_url,
            json=data,
            headers=header
        )
        # print(response.json())
        # print(response.json())
        # print(response.json()['user'])
        # print(response.json()['token'])
        self.token = response.json()['token']
        self.status = response.status_code
        self.user = response.json()['user']
        return self.token




    def status_code_is_200(self):
        return self.status == 200

    def name_of_user_the_same_as_sent(self):
        return self.name == self.user

    def token_is_not_empty(self):
        return len(self.token) > 0
