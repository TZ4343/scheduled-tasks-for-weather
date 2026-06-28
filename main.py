import requests
import os
# credits:https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
api_key = "a4659da27cf7063a9392f4c0a6ce13bc"
MY_LAT = 41.878113
MY_LONG = -87.629799

#used in Environment Variable thing on the terminal used:$env:botchatID = "8357778629"
#used import os then os.environ.get("key") has to be run from terminal doesnt work with the run button in pycharm
#to run code do python main.py at least on my machine

def telegram_bot_sendtext(bot_message):
    bot_token = os.environ.get("key")
    bot_chatID = os.environ.get("botchatID")
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

things = {
    "lat":MY_LAT,
    "lon": MY_LONG,
    "cnt": 4,
    "appid":api_key,
}

with requests.get("https://api.openweathermap.org/data/2.5/forecast",params=things) as connections:
    connections.raise_for_status()
    data = connections.json()
    # print(data["list"][0]["weather"][0]["id"])
    # print(data["list"])
    will_rain = False
    for item in data["list"]:
        curr_max = item["weather"][0]["id"]
        if curr_max < 700:
            will_rain = True

if will_rain:
    test = telegram_bot_sendtext("Its gonna Rain get an Umbrella Bro")
