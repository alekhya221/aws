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
    def __init__(self,name=None,age=None,score=None):
        self.name = name
        self.age=age
        self.score=score
        self.student_id=None
        
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
                print(*data)
        
            
s1=Student.get(student_id=1)