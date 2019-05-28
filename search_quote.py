import urllib.parse
from urllib import request

url = 'http://www.baidu.com/s?wd='
headers = {
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",

}
key = input('请输入搜索的内容')

params = urllib.parse.quote(key)
url += params

print('***' + url + "****")

req = request.Request(url, headers=headers)

res = request.urlopen(req)

html = res.read().decode("utf-8")

filename = '%s.html' % key

with open(filename, 'w') as f:
    f.write(html)
