import pymongo

'''
库：aid1901
集合 ：student
文档
'''

# 链接对象
conn = pymongo.MongoClient('localhost', 27017)
# 库对象
db = conn.paBug
# 集合对象
myset = db.student
# 插入语句
myset.insert_one({"姓名": '唐伯虎', "年龄": "23"})
