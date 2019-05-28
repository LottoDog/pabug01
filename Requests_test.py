import requests

url = 'http://www.baidu.com/'
headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",

}

res = requests.get(url, headers=headers)
# 获取响应内容-直接获取字符串res.text
res.encoding = 'utf-8'
# print(res.encoding)

#bytes格式
#当非结构化数据时（图片/音视频）
print(res.content)

# print(res.text)

#获得响应码
print(res.status_code)
