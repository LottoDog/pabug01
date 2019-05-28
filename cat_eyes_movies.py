from urllib import request
import re, pymongo


class Cat_Eyes_Movies():
    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['paBug']
        self.table = self.db['movies']
        self.url = 'https://maoyan.com/board'
        self.haeders = {
            'User-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
        }

    def get_page(self, url):
        req = request.Request(url, headers=self.haeders)
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parse_page(html)

    def parse_page(self, html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        movies_list = p.findall(html)
        for r in movies_list:

            print(r[0].strip(), r[1].strip()[3:], r[2][5:15])
            self.table.insert_one({
                "名称": r[0].strip(),
                "主演": r[1].strip()[3:],
                "上映日期": r[2][5:15]

                                   })

    def main(self):
        self.get_page(self.url)


if __name__ == "__main__":
    cat = Cat_Eyes_Movies()
    cat.main()
