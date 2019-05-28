from urllib import parse, request


# 1分析url规律
# f?kw=xx&pn=50*(n-1)


class TieBa(object):
    def __init__(self):
        self.headers = {
            'User=agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

    # 获取响应内容
    def get_page(self, url):
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    # 解析页面
    def parse_page(self):
        pass

    # 保存数据
    def write_page(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    # 主函数
    def main(self):
        # 输入贴吧名，起止页码
        name = input('请输入贴吧名')
        start = int(input('请输入起始页'))
        end = int(input('请输入终止页'))
        # 拼接地址
        for page in range(start, end + 1):
            pn = 50 * (page - 1)
            params = parse.urlencode({'kw': name, 'pn': str(pn)})
            url = 'http://tieba.baidu.com/f?' + params
            print(url)
            html = self.get_page(url)
            filename = '{}-第{}页.html'.format(name, str(page))
            self.write_page(filename, html)
            print('第%d页爬取成功！' % page)


if __name__ == '__main__':
    t = TieBa()
    t.main()
