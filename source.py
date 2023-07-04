import requests
import configparser
import os
import time

CONFIG_FILE = 'config.ini'
REQUEST_INTERVAL = 8

def get_authorization_token():
    if os.path.exists(CONFIG_FILE):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        if 'Authorization' in config['DEFAULT']:
            return config['DEFAULT']['Authorization']

    authorization_token = input("Enter your authorization token: ")
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'Authorization': authorization_token}
    with open(CONFIG_FILE, 'w') as config_file:
        config.write(config_file)
    
    return authorization_token

def send_typing_request(channel_id, authorization_token, request_count):
    url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
    headers = {
        'Authorization': authorization_token
    }
    response = requests.post(url, headers=headers)
    
    if response.status_code == 204:
        print(f"Request #{request_count} - Typing request sent successfully.")
    else:
        print(f"Request #{request_count} - Failed to send typing request.")
        print("Response:", response.text)

def main():
    authorization_token = get_authorization_token()
    channel_id = input("Enter the channel ID: ")
    
    request_count = 1
    while True:
        send_typing_request(channel_id, authorization_token, request_count)
        request_count += 1
        time.sleep(REQUEST_INTERVAL)

if __name__ == "__main__":
    main()
