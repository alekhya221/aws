def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
	
class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
    pass
class InvalidField(Exception):
    pass



class Student:
    def __init__(self,student_id=None,name=None,age=None,score=None):
        self.student_id=student_id
        self.name = name
        self.age=age
        self.score=score
        print(self.student_id)
        print(self.name)
        print(self.age)
        print(self.score)
                
        
    @classmethod
    def get(cls,**kwargs):
        
        for k,v in kwargs.items():
            
            if 'student_id'==k:
                data = read_data("select * from Student where student_id = {}".format(v))
            elif 'name' == k:
                data = read_data("select * from Student where name like '%{}%'".format(v))
            elif 'age' == k:
                data = read_data("select * from Student where age={}".format(v))
            elif 'score' == k:
                data = read_data("select * from Student where score={}".format(v))
            
            else:
                raise InvalidField
                
            
            if len(data)>1:
                raise MultipleObjectsReturned
            elif len(data)==0:
                raise DoesNotExist
            else:
                return Student(*data[0])
    def delete(self):
        write_data("delete from Student where student_id = {}".format(self.student_id))
        
    def save(self):
        import sqlite3
        conn = sqlite3.connect('students.sqlite3')
        c=conn.cursor()
        if self.student_id == None:
            c.execute("insert into Student(name,age,score) values(?,?,?)",(self.name,self.age,self.score))
            self.student_id = c.lastrowid
        elif self.student_id != None:
            c.execute("insert or replace into Student(student_id,name,age,score) values (?,?,?,?)",(self.student_id,self.name,self.age,self.score))
        else:
            c.execute("update Student set name=?,age=?,score=? where student_id=?",(self.name,self.age,self.score,self.student_id))
            
        conn.commit()
        conn.close()
           
                   
    

s1=Student.get(student_id=1)
print(s1.name)
#print(s1.student_id)
#print(s1.age)
#print(s1.score)























"""class DoesNotExist(Exception):
	pass

class MultipleObjectsReturned(Exception):
	pass

class InvalidField(Exception):
	pass

class Student:
	def __init__(self, name, age, score):
		self.name = name
		self.student_id = None
		self.age = age
		self.score = score

	@staticmethod
	def get(**kwargs):
		for key, value in kwargs.items():
			key_attribute = key
			value = value

		if key_attribute not in ("student_id", "name", "age", "score"):
			raise InvalidField
		if key_attribute == "name":
			sql_query = read_data(f"SELECT * FROM Student WHERE {key_attribute} = '{value}'")
		else:
			sql_query = read_data(f"SELECT * FROM Student WHERE {key_attribute} = {value}")
	
		if len(sql_query) == 0:
			raise DoesNotExist
			
		elif len(sql_query) > 1:
			raise MultipleObjectsReturned
		else:
			ans = Student(sql_query[0][1], sql_query[0][2], sql_query[0][3])
			ans.student_id = sql_query[0][0]
			return ans
		
	def save(self):
		import sqlite3
		conn = sqlite3.connect("students.sqlite3")
		c = conn.cursor() 
		c.execute("PRAGMA foreign_keys=on;")
		
		if self.student_id == None:
			c.execute(f"INSERT INTO Student (name, age, score) values ('{self.name}', {self.age}, {self.score})")        
			self.student_id = c.lastrowid
		else:
			c.execute(f"UPDATE Student SET name = \'{self.name}\', age = {self.age}, score = {self.score} WHERE student_id = {self.student_id}")
		conn.commit() 
		conn.close()

	def delete(self):
	    write_data(f"DELETE FROM Student WHERE student_id = {self.student_id}")
	
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query)
	ans= crsr.fetchall()
	connection.close()
	return ans
	
"""



























