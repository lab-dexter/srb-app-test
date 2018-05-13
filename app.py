import MySQLdb
import os

user = os.environ["MYSQL_USER"]
passwd = os.environ["MYSQL_PASSWORD"]
dbhost = os.environ["MYSQL_SERVICE_HOST"]
dbname = os.environ["MYSQL_DATABASE"]

db = MySQLdb.connect(host=dbhost,
                     user=user,
                     passwd=passwd,
                     db=dbname)


cur = db.cursor()

cur.execute("SELECT * FROM `sensor_data`")

for row in cur.fetchall():
  print("{} {} {}".format(row[0], row[1], row[2]))