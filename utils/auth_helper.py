class AuthHelper:
    def __init__(self,api_client):
        self.api_client = api_client

    def get_access_token(self):

        payload = {
            "username": "emilys",
            "password" :  "emilyspass"
        }

        response = self.api_client.post("/auth/login",payload = payload)

        assert response.status_code == 200, ( f"Login failed: {response.status_code} - {response.text}")

        response_data = response.json()

        token = response_data.get("accessToken")

        assert token, "Access token not found in login response"

        return token