import pymysql
DBHOST = '127.0.0.1'
DBUSER = 'root'
DBPASS = 'hfk7613373'
DBNAME = 'test'

'''
updata data
'''
try:
    db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("数据库成功连接")
    cur = db.cursor()
    sql = 'UPDATE Student set Name = %s where Name = %s'
    value = ('John', 'Mike')
    cur.execute(sql, value)
    db.commit()
    print("updata data success")

except pymysql.Error as e:
    print("data updata failue：" + str(e))
    db.rollback()

db.close()