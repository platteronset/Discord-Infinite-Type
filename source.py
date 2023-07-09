import requests
import configparser
import os
import time
from colorama import init, Fore
from concurrent import futures

CONFIG_FILE = 'config.ini'
ID_FILE = 'channel_ids.txt'
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

def save_channel_ids(ids):
    with open(ID_FILE, 'w') as id_file:
        id_file.write(','.join(ids))

def read_channel_ids():
    if os.path.exists(ID_FILE):
        use_existing_ids = input("A channel ID file already exists. Do you want to use the saved ID(s)? (y/n): ")
        if use_existing_ids.lower() == 'y':
            with open(ID_FILE, 'r') as id_file:
                return id_file.read().split(',')

    id_list = input("Enter the channel ID(s) (separated by commas if multiple): ")
    return [id.strip() for id in id_list.split(',')]

def send_typing_request(channel_id, authorization_token, request_count):
    url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
    headers = {
        'Authorization': authorization_token
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 204:
        print(f"{Fore.GREEN}Request #{request_count} - Typing request sent successfully. Channel ID: {channel_id}{Fore.RESET}")
    else:
        print(f"{Fore.RED}Request #{request_count} - Failed to send typing request. Channel ID: {channel_id}{Fore.RESET}")
        print("Response:", response.text)

def main():
    init(autoreset=True)

    authorization_token = get_authorization_token()

    option = input("Choose an option:\n[1] Read ID(s) from a list\n")

    if option == '1':
        id_list = read_channel_ids()
        save_channel_ids(id_list)

        request_count = {channel_id: 1 for channel_id in id_list}
        while True:
            with futures.ThreadPoolExecutor() as executor:
                request_futures = []
                for channel_id in id_list:
                    request_futures.append(executor.submit(send_typing_request, channel_id, authorization_token, request_count[channel_id]))
                    request_count[channel_id] += 1

                futures.wait(request_futures)

            time.sleep(REQUEST_INTERVAL)

    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    main()
