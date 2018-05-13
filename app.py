import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",
                     user="remote-admin",
                     passwd="Some-pass!23",
                     db="smart-recycling-bins")

cur = db.cursor()

cur.execute("SELECT * FROM `00-00-00-00-00-00_1`")

for row in cur.fetchall():
  print row[0], " ", row[1], " ", row[2]