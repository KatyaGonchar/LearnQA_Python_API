import requests
import json

expected_value = {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}

response = requests.get(
    "https://playground.learnqa.ru/ajax/api/user_agent_check",
    headers={"User-Agent": 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'}
)

print(response.content)

values = json.loads(response.content)

assert expected_value['platform'] == values['platform'], "Platform not match"
assert expected_value['browser'] == values['browser'], "Browser not match"
assert expected_value['device'] == values['device'], "Device not match"