import os
import requests

def main():
    # Access the secret keys
    secret_key_1 = os.getenv("SECRET_KEY_1")
    secret_key_2 = os.getenv("SECRET_KEY_2")
    if secret_key_1:
        print(f"Secret Key 1: {secret_key_1}")
        print(f"Secret Key 2: {secret_key_2}")
    else:
        print("secret key not found")

    # Use the keys as needed
    print("Hi, Before Sending")

    apiURL = f'https://api.telegram.org/bot{secret_key_1}/sendMessage'
    message = "Hi, Welcome to Github Actions"
    print(apiURL)
    try:
        response = requests.post(apiURL, json={'chat_id': secret_key_2, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

    print("Hi, Before Sending")

if __name__ == "__main__":
    main()
