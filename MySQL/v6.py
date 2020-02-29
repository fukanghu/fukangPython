import pymysql
DBHOST = '127.0.0.1'
DBUSER = 'root'
DBPASS = 'hfk7613373'
DBNAME = 'test'

'''
delete data
'''
try:
    db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("数据库成功连接")
    cur = db.cursor()
    sql = 'DROP TABLE IF EXISTS Student'
    cur.execute(sql)
    db.commit()
    print("delete table success")

except pymysql.Error as e:
    print("table delete failue：" + str(e))
    db.rollback()

db.close()