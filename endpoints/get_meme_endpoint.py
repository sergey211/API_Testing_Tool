import requests
from endpoints.endpoint_handler import Endpoint


class MemeEndpoint(Endpoint):
    token = None
    user = None
    long_url = None
    max_id = None
    resp_text = None

    def __init__(self, token):
        # base_url = self.long_url - WRONG!
        self.token = token
        self.url = 'http://okulik.site:52355/meme'

    def get_meme_max(self):
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
        # print(response.json())
    #    print(response.json()['data'][-1]['id'])
        listMems = response.json()['data']
        listId = []
        for x in listMems:
            listId.append(x['id'])
        # print(listId)
        # print(len(listId))
        # print(sorted(listId))
        max_id = max(listId)
        # print(max_id)
        return max_id

    def get_meme_unauth(self):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

        response = requests.get(
            self.url,
            headers=header
        )
        self.status = response.status_code
        return response.text

    def get_mem_by_id(self, id):
        header = {
            'Content-Type': 'application/json',
            'Authorization': self.token
        }

        response = requests.get(
            self.url+'/'+str(id),
            headers=header
        )
        # resp_text = response.text
        # print(resp_text)
        self.status = response.status_code
        print(self.status)
        return response.text