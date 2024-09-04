import requests
import json
import sys

# Define the URL and headers
url = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

if len(sys.argv) > 1:
    question=sys.argv[1]
else:
    question=input("Ask me anything: ")

# Define the payload
payload = {
    "model": "llama3",
    "prompt": question,
    "stream": False 
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
if response.status_code == 200:
    response_json = response.json()
    print("Response:", response_json.get('response'))
else:
    print("Failed to get a response. Status code:", response.status_code)
