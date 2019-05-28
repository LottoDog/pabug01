from urllib import request
import re, csv, time


class Dytt(object):
    def __init__(self):
        self.headers = {
            'User=agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",

        }
        self.url = "https://www.dytt8.net/html/gndy/dyzz/index.html"
        self.url2 = "https://www.dytt8.net"

    def get_request(self):
        req = request.Request(self.url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('gb18030')

        return html

    def get_parse(self, html):
        pattern = re.compile('''<table width="100%".*?<a href="(.*?)".*?>(.*?)</a>.*?</table>''', re.S)
        info_list = pattern.findall(html)
        url2 = []
        with open('DYTT.csv', 'w') as f:
            writer = csv.writer(f)
            for i in info_list:
                writer.writerow([
                    #0为地址,1为名字
                    i[1], i[0]
                ])
                # 将新的二级地址拼接放入url2备用
                url2.append(self.url2 + i[0])
            print(url2)
            # 循环替换self.url
            for u2 in url2:
                self.url = u2
                print(self.url)
                # 调用get_request

                html2 = self.get_request()
                # get_parse2()
                self.get_parse2(html2)

        return "200ok"

    def get_parse2(self, html2):
        pattern2 = re.compile(
            '<tbody>.*?href="(.*?)">.*?</a>',
            re.S)
        FTP_list = pattern2.findall(html2)

        with open('FTP.csv', 'a') as f:
            writer = csv.writer(f)
            for i in FTP_list:
                writer.writerow([
                    i
                ])
        print(FTP_list)


    def main(self):
        html = self.get_request()
        self.get_parse(html)


if __name__ == "__main__":
    d = Dytt()
    d.main()
