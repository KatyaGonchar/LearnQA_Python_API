import requests

response_history = requests.get('https://playground.learnqa.ru/api/long_redirect').history
counter = 0
if response_history:
    for resp in response_history:
        counter += 1


print(f'Redirects {counter}')
print(f'Last url  {response_history[counter - 1].url}')