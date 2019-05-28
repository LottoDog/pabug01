from urllib import request
import re, pymysql


class Cat_Eyes_Movies():
    def __init__(self):

        self.db = pymysql.connect(
            'localhost',
            'root',
            '123456',
            'paBug',
            charset='utf8'
        )
        self.cur = self.db.cursor()

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
            info = 'insert into movies values (%s,%s,%s);'
            self.cur.execute(info, [r[0].strip(), r[1].strip()[3:], r[2][5:15]])
            self.db.commit()
        







    def main(self):
        self.get_page(self.url)

        self.cur.close()
        self.db.close()


if __name__ == "__main__":
    cat = Cat_Eyes_Movies()
    cat.main()
