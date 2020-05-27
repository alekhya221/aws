import sqlite3
conn = sqlite3.connect('Students.sqlite3')

c = conn.cursor()

c.execute("""creart table Student(student_id integer auto incrementname text,age integer,score integer)""")    

conn.commit()
conn.close()
