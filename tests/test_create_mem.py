import requests

def test_create_mem():
    header = {'Content-Type': 'application/json'}
    data = {
        'input': 'http://okulik.site:52355/'
    }
    responce = requests.post()
