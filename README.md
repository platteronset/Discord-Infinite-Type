# Discord Infinite Type

This Python script sends typing indicator requests to multiple Discord channels simultaneously. It can be used to simulate typing activity in channels, providing an indication that someone is actively engaging.

## Installation

1. Clone the repository or download the script file.

2. Install the required dependencies by running the following command: pip install requests configparser colorama

## Usage

1. Obtain an authorization token from Discord. You can create a bot or use your own user account.

2. Run the script: python source.py

3. Follow the prompts to enter your authorization token and choose the channel ID(s) you want to send typing requests to.

4. The script will continuously send typing requests to the specified channels at a defined interval (default: 8 seconds). Each request is counted, allowing you to track the activity.

## Configuration

The script uses a configuration file (`config.ini`) and a channel ID file (`channel_ids.txt`) to store and retrieve authorization information and channel IDs respectively.

If the `config.ini` file exists and contains an 'Authorization' field, it will be used automatically. Otherwise, you will be prompted to enter your authorization token.

If the `channel_ids.txt` file exists, you can choose to use the saved IDs instead of entering them manually.

## Note

- Make sure you have the necessary permissions to send messages in the target channels.

- Be mindful of Discord's API rate limits to avoid potential restrictions or penalties.

- This script uses the `concurrent.futures` module to send requests concurrently, improving efficiency.
