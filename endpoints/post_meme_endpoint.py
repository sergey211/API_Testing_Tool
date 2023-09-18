import requests
from endpoints.endpoint_handler import Endpoint


class PostMemeEndpoint(Endpoint):
    token = None
    meme_id = None
    responce = None

    def __init__(self, token, data=None):
        # base_url = self.long_url - WRONG!
        self.token = token
        self.url = 'http://okulik.site:52355/meme'
        if data==None:
            self.data = {
                "text": "test",
                "url": "test",
                "tags": ["test"],
                "info": {"key1": "key2"}
            }
        else:
            self.data = data

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
      #  self.response = response.json()
        self.response = response
        print(response.text)
        print(self.response)
        print('post self.data = ', self.data)
        print(self.response.text)
   #     print(response.json()['id'])
#        print(self.response.json()['id'])
        try:
            self.meme_id = response.json()['id']  # works if not 500
            return self.response.json()['id']  # works if not 500
        except:
            print('Cannot find ID')
#         print(self.meme_id)




