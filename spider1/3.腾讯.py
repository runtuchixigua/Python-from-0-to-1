import json
import requests

res = requests.post(
    url="https://ke.qq.com/cgi-proxy/course_list/search_course_list?bkn=&r=0.1649",
    data=json.dumps({"mt":"1001","st":"2056","page":"2","visitor_id":"9340935770592473","finger_id":"a9d61dde57ac8f4694860da1e9952a3b","platform":3,"source":"search","count":24,"need_filter_contact_labels":1}),
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Referer":"https://ke.qq.com/course/list?mt=1001&quicklink=1&st=2056&page=2",
        "Content-Type":"application/json;charset=utf-8"
    }
)

print(res.text)