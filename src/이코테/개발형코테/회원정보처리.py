import requests

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

data = response.json()

new_list = []
for user in data:
	new_list.append(user['name'])

print(new_list)