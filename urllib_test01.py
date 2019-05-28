import urllib.request as ul

r = ul.urlopen("http://httpbin.org/get")
print(r)
html = r.read().decode('utf-8')
print(html)
print(type(html))