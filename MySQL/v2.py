import pymysql
DBHOST = '127.0.0.1'
DBUSER = 'root'
DBPASS = 'hfk7613373'
DBNAME = 'test'

'''
insert data
'''
try:
    db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("数据库成功连接")
    cur = db.cursor()
    sql = 'INSERT INTO Student(Name, Email, Age) VALUE(%s, %s, %s)'
    value = ('Mike', '123@123.com', 20)
    cur.execute(sql, value)
    db.commit()
    print("data insert success")
except pymysql.Error as e:
    print("data insert failue：" + str(e))
    db.rollback()

db.close()