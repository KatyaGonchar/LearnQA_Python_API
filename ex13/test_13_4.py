import requests
import json

expected_value = {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}

response = requests.get(
    "https://playground.learnqa.ru/ajax/api/user_agent_check",
    headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'}
)

print(response.content)

values = json.loads(response.content)

assert expected_value['platform'] == values['platform'], "Platform not match"
assert expected_value['browser'] == values['browser'], "Browser not match"
assert expected_value['device'] == values['device'], "Device not match"