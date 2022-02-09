from pprint import pprint
from copy import copy, deepcopy
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
        test_data = copy(TEST_DATA)
        test_data['apartaments'] = 300
        test_data['country'] = 'Україна'
        response = self.client.post(BASE_URL+'address/', 
                                    data=test_data)
        self.assertEqual(response.status_code, 201)


    def test_get_addresses(self):
        response = self.client.get(BASE_URL+'address/')
        # print(response.json())
        self.assertEqual(response.status_code, 200)

    def test_get_address(self):
        response = self.client.get(BASE_URL+'address/1/')
        self.assertEqual(response.status_code, 200)

    def test_update_address(self):
        test_data = deepcopy(TEST_DATA)
        test_data['apartaments'] = 205
        response = self.client.put(BASE_URL+'address/1/', 
                                    data=test_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_address(self):
        response = self.client.delete(BASE_URL+'address/1/')
        self.assertEqual(response.status_code, 204)

    def test_post_invalid_address(self):
        test_data = copy(TEST_DATA)
        test_data['apartaments'] = 'apartaments'
        response = self.client.post(BASE_URL+'address/', 
                                    data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('integer is required', response.json()['apartaments'][0])
        print('Test 1. Passed')
        
        test_data['apartaments'] = 0
        response = self.client.post(BASE_URL+'address/', 
                                    data=test_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('cannote be less or equal zero', response.json()['non_field_errors'][0])

        print('Test 2. Passed')

        test_data = copy(TEST_DATA)
        test_data['country'] = 'ARR2'
        response = self.client.post(BASE_URL+'address/', 
                                    data=test_data)
        self.assertEqual(response.status_code, 400)
       
        # self.assertIn('cannote be less or equal zero', response.json()['non_field_errors'][0])

        print('Test 3. Passed')

    def test_delete_undefined_address(self):
        response = self.client.delete(BASE_URL+'address/100/')
        self.assertEqual(response.status_code, 404)

    def test_post_put_duplicate_address(self):
        # POST
        response = self.client.post(BASE_URL+'address/', 
                                    data=TEST_DATA)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Address with this data is already exixts', response.json()[0])
        print('Test 1. Passed')
        
        # PUT
        test_data = copy(TEST_DATA)
        test_data['apartaments'] = 210
        response = self.client.post(BASE_URL+'address/', 
                                    data=test_data)
        response = self.client.put(BASE_URL+'address/1/', 
                                    data=test_data)
        self.assertEqual(response.status_code, 400)
        print('Test 2. Passed')

    def test_put_without_changes(self):
        response = self.client.put(BASE_URL+'address/1/', 
                                    data=TEST_DATA)
        self.assertEqual(response.status_code, 200)
        
        