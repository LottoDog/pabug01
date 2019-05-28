from urllib import request

url = 'http://httpbin.org/get'
headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",

}

req = request.Request(url, headers=headers)

res = request.urlopen(req)

html = res.read().decode("utf-8")
print(html)