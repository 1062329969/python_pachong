import pymysql
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'test',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

# Connect to the database
conn = pymysql.connect(**config)
cursor = conn.cursor()
# #执行sql，更新单条数据，并返回受影响行数
# effect_row = cursor.execute("update hosts set host = '1.1.1.2'")
# #插入多条，并返回受影响的函数
# effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)",[("1.0.0.1",1,),("10.0.0.3",2)])
#获取最新自增ID
# new_id = cursor.lastrowid
#查询数据
# cursor.execute("select * from yh_users")
#获取一行
# row_1 = cursor.fetchone()
#获取多(3)行
# row_2 = cursor.fetchmany(3)
#获取所有
# row_3 = cursor.fetchall()
#重设游标类型为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#提交，保存新建或修改的数据
conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()