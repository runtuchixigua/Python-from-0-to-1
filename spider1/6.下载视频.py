import requests

res = requests.get(
    url="https://v3-web.douyinvod.com/4f17c475df0a484a41fa1abe00f43aaa/65695cf6/video/tos/cn/tos-cn-ve-15c001-alinc2/oIrIAZg9ChRRquVyAYQdESIxNWAQzBACtzJemf/?a=6383&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1354&bt=1354&cs=0&ds=4&ft=GN7rKGVVyw3XRZ_8emo~xj7ScoAp9656EvrK-iBTkto0g3&mime_type=video_mp4&qs=0&rc=ZWU7NTo3NDc0ZDM2ODQ6OkBpM2c8ODw6Zm9qbjMzNGkzM0AxNS9eY2BjNTQxYGIvYDMwYSNgZzVpcjRnamxgLS1kLS9zcw%3D%3D&btag=e00030000&dy_q=1701400015&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20231201110655C26B991C0F271857AB12",
)
# print(res.content)

with open("v1.mp4", mode='wb') as f:
    f.write(res.content)