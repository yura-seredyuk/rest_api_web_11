import requests
from pprint import pprint

BASE_URL = 'http://127.0.0.1:8000/'

def get_list():
    response = requests.get(BASE_URL+'address/')
    pprint(response.json())

def post_address():
    data = {
        "country": "Україна",
        "city": "Рівне",
        "zip_code": 33030,
        "street": "Соборна",
        "house_num": "46",
        "apartaments": 200
    }
    response = requests.post(BASE_URL+'address/', data=data)

    print(response.json(), response.status_code)



if __name__ == '__main__':
    post_address()
    get_list()
    pass