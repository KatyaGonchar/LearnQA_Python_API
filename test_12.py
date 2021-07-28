import requests

response = requests.get("https://playground.learnqa.ru/api/homework_header").headers

headers = {'Date': 'Wed, 28 Jul 2021 17:31:10 GMT', 'Content-Type': 'application/json', 'Content-Length': '15', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10', 'Server': 'Apache', 'x-secret-homework-header': 'Some secret value', 'Cache-Control': 'max-age=0', 'Expires': 'Wed, 28 Jul 2021 17:31:10 GMT'}

print(response)

assert headers == response, "Headers doesn't match"