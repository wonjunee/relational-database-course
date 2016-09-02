import sqlite3

conn = sqlite3.connect("cookies")

c = conn.cursor()

query = "select name, id from students order by students.name;"
c.execute(query)

query = "INSERT INTO cookies VALUES (1,2,3);"
c.execute(query)

rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()
