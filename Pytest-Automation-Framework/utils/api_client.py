import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self) -> None:
        self.header={
          "Content-Type":"application/json"  
        }

    def get(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.get(url=url, headers=self.header)
        return response
    
    def post(self, endpoint, jsonData):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.post(url=url, headers=self.header, json=jsonData)
        return response
    
    def put(self, endpoint, jsonData):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.put(url=url, headers=self.header, json=jsonData)
        return response
    
    def delete(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.delete(url=url, headers=self.header)
        return response