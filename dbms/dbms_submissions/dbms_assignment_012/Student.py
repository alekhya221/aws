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
        self.name = name
        self.age=age
        self.score=score
        self.student_id=student_id
        
    @classmethod
    def get(cls,**kwargs):
        #print(kwargs)
        for k,v in kwargs.items():
            if 'student_id'==k:
                data = read_data("select * from Student where student_id = {}".format(v))
            elif 'name' == k:
                data = read_data("select * from Student where name={}".format(v))
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
                
    def save(self):
        import sqlite3
        conn = sqlite3.connect('students.sqlite3')
        c=conn.cursor()
        if self.student_id == None:
            c.execute("insert into student(name,age,score) values(?,?,?)",format(self.name,self.age,self.score))
            self.student_id = c.lastrowid
        else:
            c.execute("update student set name=?,age=?,score=? where student_id=?",format(self.name,self.age,self.score))
            
        conn.commit()
        conn.close()
            
                
    #def delete(self):
        #write_data("delete from Student where student_id = {}".format(self.student_id)
        
            
s1=Student.get(student_id=1)
print(s1.student_id)