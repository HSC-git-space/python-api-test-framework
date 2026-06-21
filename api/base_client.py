import requests
from config.config import BASE_URL, TIMEOUT, HEADERS


class BaseClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.base_url = BASE_URL
        self.timeout = TIMEOUT

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        return response

    def post(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        return response

    def put(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, timeout=self.timeout)
        response.raise_for_status()
        return response