from unittest import TestCase

import requests


class TestFlaskApiUsingRequests(TestCase):    
    def test_create(self):
        payload = {
            {"reservation_datetime":"06032020 21:00:03",
             "guest_name":  "Ramesh",
             "guest_phone":  "9740032387",
             "num_guests": "4",
             "email_id" : "champ@gmail.com"
             }
        }
        response = requests.post('http://127.0.0.1:5000/', payload)
        self.assertEqual(response.status_code, 201)
