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
cur.execute(ins, [name, star, time])
# commit
db.commit()

# 关闭
cur.close()
db.close()
