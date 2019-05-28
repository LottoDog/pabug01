#爬虫
    python优势：
        请求模块丰富成熟
        强大的网络爬虫框架SCRAPY
        多线程适合也网络IO/本地磁盘IO
    其他劣势：
        PHP多线程/异步性能差
        JAVA代码笨重,量大
        C/C++效率相当高,难度大,开发效率低,代码成型慢
    爬虫分类：
        1通用网络爬虫
            百度,谷歌..搜索引擎,百度快照就是爬取的
            遵守ROBOTS机器人协议（君子协议）
        2聚焦网络爬虫
            1URL
            2反请求获得相应
            3解析提取数据
##请求模块(标准库模块：urllib.request)
    方法：urllib.request.open(url)
    返回响应对象
    响应对象.read()返回byte字节串
    通过decode（）转为unicode字符串
    示例：
        import urllib.request as ul

        r = ul.urlopen("http://www.baidu.com/")
        print(r)
        html = r.read().decode('utf-8')
        print(html)
        print(type(html))
    
        http://httpbin.org/get
        测试网址返回请求信息
        
        一般反爬首先会检查请求头中的user-agent字段信息
        
##反爬第一步：重构headr中的user-agent
    否则urllib请求会
        {
      "args": {}, 
      "headers": {
        "Accept-Encoding": "identity", 
        "Host": "httpbin.org", 
        "User-Agent": "Python-urllib/3.6"
      }, 
      "origin": "101.206.168.116, 101.206.168.116", 
      "url": "https://httpbin.org/get"
    }
     "User-Agent": "Python-urllib/3.6"暴露
     
     但是urllib中不支持重构请求头信息  
     
     方法：Request（url,headers={}）
     import urllib.Request
     urllib.Request(url,headers={})
     作用：构造一个请求对象
     返回请求对象r
     r.rulopen(url)#发生请求

##检索参数
    问题域名中 url地址中 中文参数为16进制 转换问题
    编码模块urllib.parse
    方法：
    1 urlencode({'wd':'值'})
        返回编码后的字符串  ‘wd=xxxxxxxx’
        一般在与该值拼接
        
    保存在本地
    filename = '%s.html' % key

    with open(filename, 'w') as f:
        f.write(html)
     windows:
     gbk
     gb2312
     gb18030
     
     指定字符集
         with open(filename, 'w',encoding='gb18030') as f:
            f.write(html)
###urllib.parse.urlencode(dic)
    返回复合url格式的编码格式字符串，对中文有编码
###拼接url地址的方式
    字符串加法
    字符串格式化 占位符
    formate()方法
    'xxx.com/s?wd={}&pn{}'.formate('值1','值2'...)

###urllib.parse.quote(字符串)
    对字符串进行编码
     解码：unquote('%E8xx')
##urllib-Python3-2区别
    python2:urllib(只负责编码),urllib2（只负责发送请求）
    Python3:合并了两个子库 urllib.parse库  urllib.request库 
    
##贴吧爬取
    输入贴吧名称
    输入起始页
    输入终止页
    输出xxx吧-第几页.html
##re模块流程
    爬虫一般不用search/match 返回正则对象
    
    r_list = re.findall(pattern, html)
    或者
    先创建re编译对象：
    In [20]: p = re.compile('abc',re.S)#功能标识位
            一般匹配不匹配 换行符 \n  
            re.S针对 元字符 . 可以匹配\n 在内的所有字符
                                                                                                                                                                      

    In [21]: r_list = p.findall(html)                                                                                                                                                         

    In [22]: r_list                                                                                                                                                                           
    Out[22]: ['abc']
    
###匹配任意一个字符的方式
    .  re.S
    [\s\S]
###贪婪匹配
    匹配成功下尽可能多的匹配*/+
###非贪婪
    .*?  .+?  .??
###re分组-- ()
    解析时想要什么内容加()
    两个以上分组,先整体匹配,然后匹配()中的
        [(元组),(),()...]
        
        
##CSV-模块
    import csv
    with open('xx.csv', 'w') as f:
        初始化写入对象 writer = csv.writer(f)
        写入数据      writer.writerrow([])
    
    csv 文件多为逗号分割
    Windows中中文会发生乱码：用记事本打开,save as ansi


##反爬
    网站监测：请求速度,headers={User-agent:随机},IP随机
    1每次访问用不用的User-agent,
    准备列表存放大量UA
    2sleep
    3.
##mongoDB数据存储-pymongo
    # 链接对象
    conn = pymongo.MongoClient('localhost', 27017)
    # 库对象
    db = conn.paBug
    # 集合对象
    myset = db.student
    # 插入语句
    myset.insert_one({"姓名": '唐伯虎', "年龄": "23"})
    
    show dbs
    use 库
    show collections
    db.集合名.count()
    db.集合名.find()
    db.dropDatabase()
    
#问题
    框架中setting
    如若两个名字定义为变量用点获取不到变量,这里用列表
    db = conn['库名']
    myset = db['集合名']
    
#mysql
    import pymysql

    '''
    字段为：name;star;time
    '''
    name = input("name:")
    star = input("star:")
    time = input("time:")
    # 数据连接对象
    db = pymysql.connect(
        'localhost',
        'root',
        '123456',
        'paBug',
        charset='utf8'
    )
    # 创建游标对象
    cur = db.cursor()
    
    # sql命令
    # ins = 'insert into movies values ("火影忍者","漩涡鸣人","2019-01-21");'
    ins = 'insert into movies values (%s,%s,%s);'
    
    #列表传参****
    
    cur.execute(ins, [name, star, time])
    # commit
    db.commit()

    # 关闭
    cur.close()
    db.close()

    #删除表内容
        delete from 表名
    
    #localhost-解释
        sodo vi /etc/hosts
        会自动匹配127.0.0.1
        
        
#爬取二级页面信息-电影天堂

#新模块-requests
    * Linux :sudo pip3 install requests
    *Windows:python -m pip install requests
    
    1 requests.get(url,headers={})
    *发起请求,并得到响应对象
    res = requests.get(url, headers=headers)
    # 获取响应内容-直接获取字符串res.text
    res.encoding = 'utf-8'
    # print(res.encoding)

    #bytes格式
    #当非结构化数据时（图片/音视频）
    print(res.content)

    # print(res.text)

    #获得响应码
    print(res.status_code)
    
    #获取返回数据的url地址（发生重定向，获取正真的数据源）
    res.url


#工具-xpath
    xml查找信息的语言-也使用于html
    优势
    提取定位
    xml/html都是结构化数据
    *//祖先节点
    */父节点
    *[]条件比如同名第几个
    *@获取属性
    条件//div[@class=值]
    取值//div/a/@src
    /html/body/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div[3]/div[2]/ul/table/tbody/tr[1]/td[1]/a[2]
    *或  |
    *content()
    //div[content(@id,"qiushi_tag_")]
    查找id属性值中包含"qiushi_tag_"的div节点
    *text()获取节点的文本内容

#第三方解析库-lxml
    from lxml import etree

    # etree有一个类可以创建解析对象

    html =
    parse_html = etree.HTML(html)

    r_list = parse_html.xpath('xpath表达式')
    #返回列表


    