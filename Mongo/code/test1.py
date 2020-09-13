# # import pymongo
# #
# # client = pymongo.MongoClient()
# # db = client.dm
# # db.authenticate("dba", "dba")
# import pymongo as pm  # 确保你已经安装过pymongo了
#
# # 获取连接
# client = pm.MongoClient('localhost', 21111)  # 端口号是数值型
#
# # 连接目标数据库
# db = client.dm
#
# # 数据库用户验证
# db.authenticate("dba", "dba")
post = {
    "id": "111111",
    "level": "MVP",
    "real": 1,
    "profile": '111',
    'thumb': '2222',
    'nikename': '222',
    'follows': 20
}
#
# db.col.insert_one(post)  # 插入单个文档
#
# # 打印集合第1条记录
# <a href="/subscribe/chenhaoalex/79.html" class="b bC" onfocus="this.blur()">79</a>
## '<a href=\'/.*?\' class=\".*?\" nofocus="this\.blur\(\)">(%d*)</a>'
import pymongo

con = pymongo.MongoClient(host="localhost", port=27017)
db = con.admin
# db.authenticate("dba", "dba")
# db.admin.insert_one(post)

con.close()
