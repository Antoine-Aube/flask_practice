import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "How to make pizza", "views": 1000},
        {"likes": 20, "name": "How to do life", "views": 300},
        {"likes": 30, "name": "How to make pie", "views": 10000}]

for i in range(len(data)):
  response = requests.put(BASE + "video/" + str(i), data[i])
  print(response.json())

# response = requests.put(BASE + "video/3", {"likes": 10, "name": "Antoine", "views": 1000})
# print(response.json())
input()
response = requests.delete(BASE + "video/0")
print(response)

input()
response = requests.get(BASE + "video/6")
print(response.json())

input()
response = requests.get(BASE + "/videos")
print(response.json())