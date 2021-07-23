import requests

response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.content.decode('utf-8'))

response1 = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response1.content)

response2 = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': 'POST'})
print(response2.content.decode('utf-8'))

methods = ['POST', 'GET', 'PUT', 'DELETE']

# POST Requests
for method in methods:
    response_post = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': method})
    print(f'POST Requests. {method} - {response_post.content}')

# GET Requests
for method in methods:
    response_get = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={'method': method})
    print(f'GET Requests. {method} -{response_get.content}')

# PUT Requests
for method in methods:
    response_put = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': method})
    print(f'PUT Requests. {method} - {response_put.content}')

# DELETE Requests
for method in methods:
    response_delete = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type', data={'method': method})
    print(f'DELETE Requests. {method} - {response_delete.content}')