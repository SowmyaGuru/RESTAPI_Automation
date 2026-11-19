import requests

base_url = "https://dummyjson.com"

response = requests.get(f"{base_url}/products",timeout=10)

print("Status Code : ",response.status_code)
print("Response Body: ", response.json())

assert  response.status_code == 200