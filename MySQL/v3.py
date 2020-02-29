import pymysql
DBHOST = '127.0.0.1'
DBUSER = 'root'
DBPASS = 'hfk7613373'
DBNAME = 'test'

'''
search data
'''
try:
    db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("数据库成功连接")
    cur = db.cursor()
    sql = 'SELECT * FROM Student'
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        Name = row[0]
        Email = row[1]
        Age = row[2]
        print('Name:%s, Email:%s, Age:%s' % (Name, Email, Age))
except pymysql.Error as e:
    print("data search failue：" + str(e))
    db.rollback()

db.close()