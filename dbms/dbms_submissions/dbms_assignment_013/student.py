def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
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
        #print(self.student_id)
        #print(self.name)
        #print(self.age)
        #print(self.score)
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
                
        
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
            if len(data)==0:
                raise DoesNotExist
            else:
                return Student(*data[0])
                
    
                
    def delete(self):
        write_data("delete from Student where student_id = {}".format(self.student_id))
     
     
        
    def save(self):
        import sqlite3
        conn = sqlite3.connect('selected_students.sqlite3')
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
        
    
    
    @classmethod
    def filter(cls,**kwargs):
    
        for k,v in kwargs.items():
            x = k.split('__')
            if x[0] not in ('student_id','name','age','score'):
                raise InvalidField
            if k in ('student_id','age','score'):
                data = read_data("select * from Student where {} = {}".format(k,v))
            elif k in ('name'):
                data = read_data("select * from Student where {} like '%{}%'".format(k,v))
                
            else:
                x  = k.split('__')
                if len(x)>1:
                    if x[1] == 'lt':
                        data = read_data("select * from Student where {} < {}".format(x[0],v))
                    elif x[1] == 'lte':
                        data = read_data("select * from Student where {} <= {}".format(x[0],v))
                    elif x[1] == 'gt':
                        data = read_data("select * from Student where {} > {}".format(x[0],v))
                    elif x[1] == 'gte':
                        data = read_data("select * from Student where {} >= {}".format(x[0],v))
                    elif x[1] == 'neq':
                        if x[0] in ['age','score','student_id']:
                            data = read_data('''select * from Student where {} <> {}'''.format(x[0],v))
                    
                        elif x[0] == 'name':
                            data = read_data('''select * from Student where {} <> "%{}%"'''.format(x[0],v))
    
                    elif x[1] == 'in':
                        data = read_data("select * from Student where {} in {}".format(x[0],tuple(v)))
                    elif x[1] == 'contains':
                       data = read_data("select * from Student where {} like '%{}%'".format(x[0],v))
            
            
            output = []
            if len(data)!=0:
                for i in range(len(data)):
                    obj = Student(*data[i])
                    output.append(obj)
            else:
                return []
        return output
            
        
        
           
              
    
#selected_students = Student.filter(age=40)
#print(Student.filter(age=100))
#selected_students = Student.filter(age=34, name="Jesse Couch")
#selected_students = Student.filter(age__lt=30)
#selected_students = Student.filter(age__lte=30)
#selected_students = Student.filter(age__neq=34)
#selected_students = Student.filter(name__contains='Jesse')
#print(selected_students)
#ages = [25, 34]
#selected_students = Student.filter(age__in=ages)
#print(selected_students)





































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
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            self.student_id,
            self.name,
            self.age,
            self.score)
        
    @staticmethod
    def get(**kwargs):
        for key, value in kwargs.items():
            if key not in ("student_id", "name", "age", "score"):
                raise InvalidField
        sql_query = read_data(f"SELECT * FROM Student WHERE {key} = '{value}'")
        
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
        conn = sqlite3.connect("selected_students.sqlite3")
        c = conn.cursor() 
        c.execute("PRAGMA foreign_keys=on;")
        
        if self.student_id == None:
            c.execute(f"INSERT INTO Student (name, age, score) values ('{self.name}', {self.age}, {self.score})")        
            self.student_id = c.lastrowid
        
        elif c.execute(f"SELECT {self.student_id} not in (SELECT student_id FROM Student) FROM Student"):
            c.execute(f"REPLACE INTO Student (student_id, name, age, score) values ({self.student_id}, '{self.name}', {self.age}, {self.score})")        
            
        else:
            c.execute(f"UPDATE Student SET name = '{self.name}', age = {self.age}, score = {self.score} WHERE student_id = {self.student_id}")
        
        conn.commit() 
        conn.close()
        
    def delete(self):
        write_data(f"DELETE FROM Student WHERE student_id = {self.student_id}")
        
    @staticmethod    
    def filter(**kwargs):
        for key, value in kwargs.items():
            key = key
            value = value
        if key not in ("student_id", "name", "age", "score"):
            raise InvalidField
        sql_query = read_data(f"SELECT * FROM Student WHERE {key} = '{value}'")
        if len(sql_query) == 0:
            return []
        else:
            ans = Student(sql_query[0][1], sql_query[0][2], sql_query[0][3])
            ans.student_id = sql_query[0][0]
            return ans

def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor()
	crsr.execute(sql_query)
	ans= crsr.fetchall()
	connection.close()
	return ans
"""















