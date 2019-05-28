from urllib import request
import re, time


class Building(object):
    def __init__(self):
        self.url = 'http://hhht.fang.lianjia.com/loupan/pg'
        self.headers = {
            'User=agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"

        }

    def get_request(self, filename, url):
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.get_parse(filename, html)

    def get_parse(self, filename, html):
        pattern = re.compile(
            '<div class="resblock-name">.*?>(.*?)</a>.*?<span class="number">(.*?)</span>',
            re.S)
        res_list = pattern.findall(html)
        info = ''
        for i in range(0, 10):
            info = info + res_list[i][0] + res_list[i][1] + "\n"
        with open(filename, 'w') as f:
            f.write(info)

    def main(self):
        start = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        for i in range(start, end + 1):
            time.sleep(2)
            url = self.url + str(i)
            filename = '链家第%d页.txt' % i
            self.get_request(filename, url)


if __name__ == "__main__":
    b = Building()
    b.main()
