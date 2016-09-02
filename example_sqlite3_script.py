import sqlite3

conn = sqlite3.connect("cookies")

c = conn.cursor()

# query = "select name, id from students order by students.name;"
# c.execute(query)

query = """
DROP TABLE IF EXISTS `document_contents`;
"""
c.execute(query)

query ="""
CREATE TABLE `document_contents` (
  `id` int(11) NOT NULL,
  `document_id` int(11) DEFAULT NULL,
  `body` text,
  PRIMARY KEY (`id`)
);
"""
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
