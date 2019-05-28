# 爬取猫眼电影排行榜10页数据打包到本地
from urllib import request
import re, time, csv
from User_agent import ua_list
import random


class Cat_Eyes_Spider(object):
    def __init__(self):
        self.url = 'http://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",

        }

    def get_request(self, filename, url):
        #random.choice,保证每次请求变化一次headers
        self.headers = random.choice(ua_list)
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.get_parse(filename, html)

    def get_parse(self, filename, html):
        pattern = re.compile(
            '<i class="board-index board-index.*?">(.*?)</i>.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            re.S)
        movies_list = pattern.findall(html)

        # content = ''
        # for t in movies_list:
        #     content = content + t[0] + t[1] + t[2].strip() + t[3] + '\n'
        #
        # with open(filename, 'w') as f:
        #     f.write(content)
        # return '200-oko'

        # 生成csv文件
        self.write_csv(filename, movies_list)

    def write_csv(self, filename, movies_list):
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for m in movies_list:
                # 元组变列表可以直接list（m）,这里构造
                L = [
                    m[0].strip(),
                    m[1].strip(),
                    m[2].strip(),
                    m[3].strip()[5:15],
                ]
                writer.writerow(L)

    def main(self):
        start = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        for r in range(start, end + 1):
            url = self.url.format(str(10 * (r - 1)))
            filename = '电影排行榜第%s页.csv' % str(r)
            time.sleep(1)
            self.get_request(filename, url)
            print('第%d页' % r)


if __name__ == "__main__":
    c = Cat_Eyes_Spider()
    c.main()
