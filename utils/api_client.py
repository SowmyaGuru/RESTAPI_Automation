import requests
from config.config import BASE_URL, TIMEOUT


class APIClient:

    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, params=None, headers=None):
        url = self.base_url + endpoint

        return requests.get(
            url,
            params=params,
            headers=headers,
            timeout=TIMEOUT
        )

    def post(self, endpoint, payload=None, headers=None):
        url = self.base_url + endpoint

        return requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=TIMEOUT
        )