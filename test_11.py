import requests

response = requests.get("https://playground.learnqa.ru/api/homework_cookie").cookies

print(response)

assert response, "Cookie exists"