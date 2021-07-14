import requests

response = requests.get('https://playground.learnqa.ru/api/get_text')

if response:
    print(response.content.decode("utf-8"))
else:
    print('An error has occurred.')