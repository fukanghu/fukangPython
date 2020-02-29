import pymysql
DBHOST = '127.0.0.1'
DBUSER = 'root'
DBPASS = 'hfk7613373'
DBNAME = 'test'

try:
    db = pymysql.connect(DBHOST, DBUSER, DBPASS, DBNAME)
    print("数据库成功连接")
    cur = db.cursor()
    cur.execute("DROP TABLE IF EXISITS Student")
    sql = 'CREATE TABLE Student(name CHAR(20), NOT NULL, Email CHAR(20), Age int))'
    print("表格创建成功")
except pymysql.Error as e:
    print("表格创建失败：" + str(e))