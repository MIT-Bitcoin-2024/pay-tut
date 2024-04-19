import os
import dotenv
import requests
dotenv.load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
print(api_key)
print(base_url)

# note this is an old pay hash
url = f"https://{base_url}/api/v1/payments/d810916c125b1eb8b25c9133e2d32c5997ce3094e9f4216982180e02f58e06e2" 

headers = {
"X-Api-Key": api_key,
"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, )

print(response)

print(response.json())
