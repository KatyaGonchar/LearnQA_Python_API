import time

import requests
import json

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

response = requests.get(url)

if response:
    x = json.loads(response.content)
    print(response.content)
    not_finished_task = requests.get(url, params={'token': x['token']}).content

    if not_finished_task:
        st = json.loads(not_finished_task)
        print(st)
        if st['status'] == 'Job is NOT ready':
            print('Status is valid')
        else:
            print('Status is invalid')

    time.sleep(x['seconds'])
    print("Import time : %s" % time.ctime())

    time.sleep(1)
    finish_response = requests.get(url, params={'token': x['token']})
    if finish_response:
        y = json.loads(finish_response.content)
        if y['status'] == 'Job is ready':
            if y['result']:
                print('Success')


