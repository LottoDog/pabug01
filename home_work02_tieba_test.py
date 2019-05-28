from urllib import request, parse


class TieBa(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?'
        self.headers = {
            'User=agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
        }

    def get_request(self, filename, url):
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.get_parse(filename, html)

    def get_parse(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    def main(self):
        name = input("请输入访问的贴吧：")
        start = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        for i in range(start, end + 1):
            pn = 50*(i-1)
            params = parse.urlencode({'kw': name, 'pn': str(pn)})
            url = self.url+params
            filename = '%s的贴吧第%d页.html' % (name, i)
            self.get_request(filename, url)


if __name__ == "__main__":
    t = TieBa()
    t.main()
