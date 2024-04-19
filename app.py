import os
import dotenv
import requests

# run pip isntall requests python-dotenv

dotenv.load_dotenv()

api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
print(api_key)
print(base_url)

headers = {
"X-Api-Key": api_key,
"Content-Type": "application/json"
}

data = {
    "out": False, 
    "amount": 10, 
    "memo": "mymemo", 
    "unit": "sat", 
}
url = f"https://{base_url}/api/v1/payments" 


response = requests.post(url, headers=headers, json=data)

print(response)

print(response.json())