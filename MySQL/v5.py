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
    sql = 'DELETE FROM Student WHERE Name = %s'
    value = ('John')
    cur.execute(sql, value)
    db.commit()
    print("delete data success")

except pymysql.Error as e:
    print("data delete failue：" + str(e))
    db.rollback()

db.close()