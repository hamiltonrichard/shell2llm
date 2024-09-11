"""
python_template.py
"""
import sys
import json
import requests

def get_question():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("Ask me anything: ")

def create_payload(question):
    return {
        "model": "llama3",
        "prompt": question,
        "stream": False
    }

def send_request(url, headers, payload):
    """Send the POST request to the API."""
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def handle_response(response):
    """Handle and print the response from the API."""
    if response.status_code == 200:
        response_json = response.json()
        print("Response:", response_json.get('response'))
    else:
        print("Failed to get a response. Status code:", response.status_code)

def main():
    """ main function """
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-type": "application/json"
    }
    question = get_question()
    print (question)
    payload = create_payload(question)
    response = send_request(url, headers, payload)
    handle_response(response)

if __name__ == "__main__":
    main()
