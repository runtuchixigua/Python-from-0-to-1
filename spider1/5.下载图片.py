import requests

res = requests.get(
    url="https://gd-hbimg.huaban.com/b93fcc5bb4751934bbd56918bdab8184966dca2974df1-bo7qSF",
)
# print(res.content)

with open("v1.png", mode='wb') as f:
    f.write(res.content)
