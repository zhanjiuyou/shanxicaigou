import pymysql

# 链接数据库,进入到shanxi这个库下面
conn = pymysql.connect(host='localhost',user='root',password='123456',port=3306,database='shanxi')
# 获取游标，后面进行sql语句的执行
cursor = conn.cursor()

title = '陕西省宝鸡市'
url = 'https://jiaokangyang.com'
date = '2020-9-26'

#  如果表不存在则创建一个表。这里切记mysql中的列名字不需要加双引号。
cursor.execute("create table if not exists shuju(id int(11) not null auto_increment primary key,title varchar(50) not null,url varchar(100) not null,riqi varchar(20) not null);")
# 将上面的三条数据插入到表中，构建sql语句
sql = "insert into shuju(title,url,riqi) values('%s','%s','%s')"%(title,url,date)
# 执行sql语句
cursor.execute(sql)
# 提交
conn.commit()
conn.close()






