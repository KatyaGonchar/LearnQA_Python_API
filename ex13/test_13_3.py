import requests
import json

expected_value = {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}

response = requests.get(
    "https://playground.learnqa.ru/ajax/api/user_agent_check",
    headers={"User-Agent": 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
)

print(response.content)

values = json.loads(response.content)

assert expected_value['platform'] == values['platform'], "Platform not match"
assert expected_value['browser'] == values['browser'], "Browser not match"
assert expected_value['device'] == values['device'], "Device not match"