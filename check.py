import os
import dotenv
import requests
dotenv.load_dotenv()
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
print(api_key)
print(base_url)

# note this is an old pay hash
url = f"https://{base_url}/api/v1/payments/d1af8ad2b0d8cfa068a66ab3f16215617eaedfda367c30fdd005efaf422ea10a" 

headers = {
"X-Api-Key": api_key,
"Content-Type": "application/json"
}

response = requests.get(url, headers=headers, )

print(response)

print(response.json())
