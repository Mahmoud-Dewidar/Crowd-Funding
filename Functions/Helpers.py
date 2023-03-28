import json
import re
import datetime

r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
r1 = "\033[0m"
g1 = "\033[0m"


# Greeting Function
def welcome():
    print(f"\n{y}##=============================================================================##")
    print(f'''{g}     __________  ________  __       ________  ________  ______   ___  ___
    |___    ___||   _____||  |     |   _____||   ____/ /  __  \ |   \/   |
        |  |    |  /_____ |  |     |  /_____ |  |     |  |  |  ||  \  /  |
        |  |    |   _____||  |     |   _____||  |     |  |  |  ||  |\/|  |
        |  |    |  /_____ |  |____ |  /_____ |  |_____|  |__|  ||  |  |  |
        |__|    |________||_______||________||_______/ \______/ |__|  |__| \n''')

    print(f'''{r}                 Welcome to the Crowd-Funding Console App!
                        Created by {g}#Mahmoud Dewidar#{g1}{r1}
                  {y}Telecom Applications Development Track''')
    print(f"{y}##=============================================================================##{r1}")


# Function to validate Egyptian phone numbers
def is_valid_phone_number(phone_number):
    regex = "01[0125][0-9]{8}"
    return re.match(regex, phone_number)


# Function to validate date format
def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


# Function to load data from JSON file
def load_json_data(file_name):
    try:
        with open(file_name, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data


# Function to save data to JSON file
def save_json_data(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
