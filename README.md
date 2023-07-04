# Typing Request Sender

This Python script sends typing requests to a Discord channel using the Discord API. Typing requests simulate a user typing in a channel and can be used to indicate activity.

## Prerequisites

Before running the script, make sure you have the following:

1. Python installed on your machine.
2. `requests` library installed. You can install it using `pip install requests`.

## Configuration

The script uses a configuration file `config.ini` to store the authorization token. If the file exists and contains an authorization token, it will be used. Otherwise, you will be prompted to enter your authorization token, and it will be stored in the configuration file for future use.

**Note: Keep your authorization token confidential and do not share it with anyone.**

## Usage

1. Clone or download the repository containing the script.
2. Open a terminal or command prompt and navigate to the script's directory.
3. Run the script using the following command:

```bash
python source.py
