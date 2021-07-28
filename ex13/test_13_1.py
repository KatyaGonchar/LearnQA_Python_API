import requests
import json

expected_value = {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'}

response = requests.get(
    "https://playground.learnqa.ru/ajax/api/user_agent_check",
    headers={"User-Agent": 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'}
)

values = json.loads(response.content)

assert expected_value['platform'] == values['platform'], "Platform not match"
assert expected_value['browser'] == values['browser'], "Browser not match"
assert expected_value['device'] == values['device'], "Device not match"