import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            with requests.get(self.url) as response:
                response.raise_for_status()
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:                return json.loads(response_body)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return None
        else:
            return None
