import requests

res = requests.get(
    url="https://api.bilibili.com/x/member/web/account?web_location=333.33",
    headers={
        "Cookie": "自己的cookie",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }
)

print(res.text)