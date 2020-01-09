import MySQLdb

db = MySQLdb.connect(host = '127.0.0.1', user = 'root', passwd='', db = 'test')
cursor = db.cursor()

create_table_sql = "CREATE TABLE IF NOT EXISTS books ( \
		id int(10) AUTO_INCREMENT PRIMARY KEY, \
	    name varchar(20)) \
	    CHARACTER SET utf8"

insert_sql = "INSERT INTO books(name) VALUES ('DjangoBook'), ('Head First')"


cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute(create_table_sql)
cursor.execute(insert_sql)

cursor.close()
db.commit()
db.close()