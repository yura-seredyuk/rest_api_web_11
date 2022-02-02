from django.test import TestCase
from rest_framework.test import APITestCase, RequestsClient

BASE_URL = 'http://127.0.0.1:8000/'

TEST_DATA = {
        "country": "USA",
        "city": "NY",
        "zip_code": 33030,
        "street": "Freedom",
        "house_num": "46",
        "apartaments": 200
    }

class API_Testing(APITestCase):
    def setUp(self):
        self.client = RequestsClient()
        response = self.client.post(BASE_URL+'address/', 
                                    data=TEST_DATA)

    def test_post_address(self):
        TEST_DATA['apartaments'] = 300
        response = self.client.post(BASE_URL+'address/', 
                                    data=TEST_DATA)
        self.assertEqual(response.status_code, 201)


    def test_get_addresses(self):
        response = self.client.get(BASE_URL+'address/')
        # print(response.json())
        self.assertEqual(response.status_code, 200)
