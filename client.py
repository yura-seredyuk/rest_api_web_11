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

def get_item(pk):
    response = requests.get(BASE_URL+f'address/{pk}/')
    pprint(response.json())

def update_address(pk):
    data = {
        "country": "Україна",
        "city": "Рівне",
        "zip_code": 33030,
        "street": "Соборна",
        "house_num": "46",
        "apartaments": 404
    }
    response = requests.put(BASE_URL+f'address/{pk}/', data=data)

    print(response, response.status_code)



if __name__ == '__main__':
    # post_address()
    # get_list()
    get_item(1)
    print('---------------')
    # update_address(1)
    # pass