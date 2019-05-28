import requests

headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",

}
url = "http://image.zhuizhuiimg.com/image/979274_1449294677.jpg"

res = requests.get(url, headers=headers)

res.encoding = 'utf-8'

html = res.content
print(res.status_code)

with open('琦玉老师.jpg', 'wb') as f:
    f.write(html)
