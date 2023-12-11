import json
import requests
import allure

BASE_URL = 'http://localhost:5555'

class UserRequest:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        
    def data(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def get_all_users():
        return requests.get(
            f'{BASE_URL}/users'
        )
    
    def get_user(self):
        return requests.get(
            f'{BASE_URL}/users/{self.id}'
        )
    
    def post(self):
        return requests.post(
            f'{BASE_URL}/users', 
            json=self.data()
        )
    
    def post_none():
        return requests.post(
            f'{BASE_URL}/users', 
            json={}
        )
    
    def post_null():
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '12398218'
        }
        return requests.post(
            f'{BASE_URL}/users', 
            headers=headers,
            json={}
        )
    
    def put(self):
        return requests.put(
            f'{BASE_URL}/users/{self.id}', 
            json=self.data()
        )
    
    def delete(self):
        return requests.delete(
            f'{BASE_URL}/users/{self.id}'
        )
    
def allure_data(title, description, severity):
    def decorator(func):
        @allure.title(title)
        @allure.description(description)
        @allure.severity(severity)
        @allure.parent_suite("Minute Media")
        @allure.suite("Tests for API features")
        @allure.label("owner", "Denis Krasilnikov")
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

def has_duplicates(json_response, key):
    # Convert JSON response to a Python data structure
    data = json.loads(json_response)

    # Check for duplicates based on the specified key
    seen_keys = set()
    for entry in data:
        entry_key = entry.get(key)
        if entry_key is not None:
            if entry_key in seen_keys:
                return True
            seen_keys.add(entry_key)

    return False

