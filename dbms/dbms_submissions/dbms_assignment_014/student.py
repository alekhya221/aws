def write_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    c = connection.cursor() 
    c.execute("PRAGMA foreign_keys=on;") 
    c.execute(sql_query) 
    connection.commit() 
    connection.close()

def read_data(sql_query):
    import sqlite3
    connection = sqlite3.connect("students.sqlite3")
    c = connection.cursor() 
    c.execute(sql_query) 
    ans= c.fetchall()  
    connection.close()
    return ans


class DoesNotExist(Exception):
    pass


class MultipleObjectsReturned(Exception):
    pass


class InvalidField(Exception):
    pass


class Student:
    def __init__(self, student_id = None ,name = None, age = None , score = None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score
        
    @staticmethod
    def aggregate(method=None,field="",**kwargs):
        #print(kwargs)
        list = ['student_id','name','age','score','']
        multiple_values = []
        
        if field not in list:
            raise InvalidField
        for k,v in kwargs.items():
            x = k.split('__')
            if x[0] not in list:
                raise InvalidField
            
            op = {'lt':'<','gt':'>','lte':'<=','gte':'>=','neq':'<>','eq':'='}
            
            if len(x) == 1:
                val = "{} {} '{}'".format(x[0],op['eq'],v)
                
            elif x[1] == 'in':
                v = tuple(v)
                val = "{} {} {}".format(x[0],'IN',v)
                
            elif x[1]=='contains':
                val = "{} {} '%{}%'".format(x[0],'LIKE',v)
            else:
                val = "{} {} '{}'".format(x[0],op[x[1]],v)
                
            #print(val)
            multiple_values.append(val)
            
        a = ' AND '.join(multiple_values)
        #print(a)
        if a=="":
            data = read_data("select {}({}) from Student".format(method,field))
        else:
            data = read_data("select {}({}) from Student where {}".format(method,field,a))
            
        return data[0][0]  
    
    @classmethod
    def avg(cls, field, **kwargs):
                
        ans = cls.aggregate('AVG', field, **kwargs)
        return ans
        
    @classmethod
    def min(cls, field, **kwargs):
        
        ans = cls.aggregate('MIN', field, **kwargs)
        return ans
        
    @classmethod
    def max(cls, field, **kwargs):
        
        ans = cls.aggregate('MAX', field, **kwargs)
        return ans
        
    @classmethod
    def sum(cls, field, **kwargs):
        
        ans = cls.aggregate('SUM', field, **kwargs)
        return ans
        
    @classmethod
    def count(cls, field = "",**kwargs):
        
        ans = cls.aggregate('COUNT', field, **kwargs)
        return ans


        
    
    
"""
#avg_age = Student.avg('age')
#avg_age = Student.avg('age', age__gt=18)
#min_age = Student.min('age', age__gt=18, age__lt=21)
#sum_of_age = Student.sum('age')
#count = Student.count()
count = Student.count('age')
#count = Student.count('age', score__gt=30, age__lt=30)
print(count)
"""

        
"""
@staticmethod    
    def aggregations(agg = None,field = "", **kwargs):
        list = ['student_id','name','age','score','']
        
        multiple_values = []
            
        if field not in list:
                raise InvalidField
                
            
        for i,j in kwargs.items():
            
            a = i.split('__')
            
            if a[0] not in list:
                raise InvalidField
                
            oper = {'gt':'>', 'lt':'<', 'lte':'<=', 'gte':'>=', 'neq':'<>', 'eq' : '='}
            
            if len(a) == 1:
                val = "{} {} '{}' ".format(a[0],oper['eq'],j)
                
            elif a[1] == 'in':
                j = tuple(j)
                val = "{} {} {}".format(a[0],'IN',j)
            
            elif a[1] == 'contains':
                val = "{} {} '%{}%' ".format(a[0],'LIKE',j)
                
            else:
                val = "{} {} '{}' ".format(a[0],oper[a[1]],j)
                
            multiple_values.append(val)
            
        x = ' AND '.join(multiple_values)
        
        if x == "":
            data = read_data("SELECT {}({}) FROM Student".format(agg,field))
        else:
            data = read_data("SELECT {}({}) FROM Student where {}".format(agg,field,x))
            
        
        return data[0][0]
        
    
        
"""    
   
"""   
   @classmethod
    def avg(cls,field,**kwargs):
        ans = cls.aggregate('AVG',field,**kwargs)
        return ans

    @classmethod
    def min(cls,field,**kwargs):
        ans = cls.aggregate('MIN',field,**kwargs)
        return ans
        
    @classmethod
    def max(cls,field,**kwargs):
        ans = cls.aggregate('MAX',field,**kwargs)
        return ans
    
    @classmethod
    def sum(cls,field,**kwargs):
        ans = cls.aggregate('SUM',field,**kwargs)
        return ans
        
    @classmethod
    def count(cls,field,**kwargs):
        ans = cls.aggregate('COUNT',field,**kwargs)
        return ans


"""






















"""
class DoesNotExist(Exception):
    pass

class MultipleObjectsReturned(Exception):
    pass

class InvalidField(Exception):
    pass

class Student:
    def __init__(self,name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    @classmethod
    def avg(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select avg({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select avg({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
    
    @classmethod
    def min(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select min({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select min({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
    
    @classmethod
    def max(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select max({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select max({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
        
    @classmethod
    def sum(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select sum({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select sum({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
        
    @classmethod
    def count(cls, field = None, **kwargs):
        if field == None:
            sql_query = "select count(*) from student"    
        
        elif field not in ('name','age','score','student_id'):
                raise InvalidField
                
        elif len(kwargs)>=1:
            sql_query = f"select count({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select count({field}) from student"        
    
        ans=read_data(sql_query)
        return ans[0][0]
    
    @staticmethod
    def filter(**kwargs):
        operator={'lt' : '<', 'lte' : '<=', 'gt' : '>', 'gte' : '>=', 'neq' : '!=', 'in' : 'in'}
        
        if(len(kwargs)) >= 1:
            conditions = []
            for key, value in kwargs.items():
                    
                    keys = key
                    keys = keys.split('__')
                    if keys[0] not in ('name', 'age', 'score', 'student_id'):
                            raise InvalidField 
            
                    if len(keys) == 1:
                        sql_query= f" {key} = '{value}'"
                    
                    elif keys[1] == 'in':
                        sql_query = f"{keys[0]} {operator[keys[1]]} {tuple(value)}"
                    
                    elif keys[1] == 'contains':
                        sql_query = f"{keys[0]} like '%{value}%'"
                    
                    else:    
                        sql_query = f"{keys[0]} {operator[keys[1]]} '{value}'"
                
                    conditions.append(sql_query)
                    
            mul_conditions = " and ".join(tuple(conditions))       
            sql_query = " " + mul_conditions
        return sql_query

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
	
	
"""	
	
















"""
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
        #print(self.student_id)
        #print(self.name)
        #print(self.age)
        #print(self.score)
    #def __repr__(self):
        #return "Student(student_id={0}, name={1}, age={2}, score={3})".format(
            #self.student_id,
            #self.name,
            #self.age,
            #self.score)
                
        
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
        conn = sqlite3.connect('students.sqlite3')
        c=conn.cursor()
        if self.student_id ==    None:
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
        
        
        
        
        
    
    @classmethod
    def avg(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select avg({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select avg({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
        
    
    @classmethod
    def min(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select min({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select min({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
        
    
    @classmethod
    def max(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select max({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select max({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
    
    @classmethod
    def sum(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select sum({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select sum({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
    
    @classmethod
    def count(cls, field, **kwargs):
        if field not in ('name', 'age', 'score', 'student_id'):
                raise InvalidField
        if len(kwargs) >= 1:
            sql_query = f"select count({field}) from student where {Student.filter(**kwargs)}"
        else:
            sql_query = f"select count({field}) from student"
    
        ans = read_data(sql_query)
        return ans[0][0]
       
        
"""       
        
    
"""
avg_age = Student.avg('age')  
#count = Student.count('age')
#print(count)
#count = Student.count('name',name = 'Sarah Kirwan')
print(avg_age)
"""

    
 
 



































  
"""    
    
@classmethod
    def avg(cls,field=None,**kwargs):
        #print(len(kwargs))
        if field in ['age','score','student_id']:
            data = read_data('select avg({}) from Student'.format(field))
            return data[0][0]
        else:
            raise InvalidField
            

    
        
    
    
    @classmethod
    def min(cls,field,**kwargs):
        if  field in ['age','score','student_id']:
            data = read_data('select min({}) from Student'.format(field))
            return data[0][0]
        else:
            raise InvalidField
                
    
    @classmethod
    def max(cls,field,**kwargs):
        if field in ['age','score','student_id']:
            data = read_data('select max({}) from Student'.format(field))
            return data[0][0]
        else:
            raise InvalidField

    
    @classmethod
    def count(cls,field,**kwargs):
        if field in ['age','score','student_id']:
            data = read_data('select count({}) from Student'.format(field))
            return data[0][0]
                    
        else:
            raise InvalidField

    @classmethod
    def sum(cls,field,**kwargs):
        if field in ['age','score','student_id']:
            data = read_data('select sum({}) from Student'.format(field))
            return data[0][0]
        else:
            raise InvalidField
"""
   
   
"""
    
    @classmethod
    def aggregate(cls,method,field,**kwargs):
        list = ['student_id','name','age','score']
        if field not in list:
            raise InvalidField
        if(len(kwargs))==0:
            if field in ['age','score','student_id']:
                data = read_data('select {}({}) from Student'.format(method,field))
                return data[0][0]
            else:
                raise InvalidField
        elif len(kwargs)==1:
            for k,v in kwargs.items():
                x = k.split('__')
                if x[0] in ['age','score','student_id']:
                    if x[1] == 'lt':
                        data = read_data('select {}({}) from Student where {} < {}'.format(method,x[0],x[0],v))
                        return data[0][0]
                    elif x[1] == 'lte':
                        data = read_data('select {}({}) from Student where {} <= {}'.format(method,x[0],x[0],v))
                        return data[0][0]
                
                    elif x[1] == 'gt':
                        data = read_data('select {}({}) from Student where {} > {}'.format(method,x[0],x[0],v))
                        return data[0][0]
                    elif x[1] == 'gte':
                        data = read_data('select {}({}) from Student where {} >= {}'.format(method,x[0],x[0],v))
                        return data[0][0]
                    elif x[1] == 'neq':
                        data = read_data('select {}({}) from Student where {} <> {}'.format(method,x[0],x[0],v))
                        return data[0][0]
                    elif x[1] == 'in':
                        data = read_data('select {}({}) from Student where {} in {}'.format(method,x[0],x[0],tuple(v)))
                        return data[0][0]
                    else:
                        data = read_data('select {}({}) from Student where {} = {}'.format(method,x[0],x[0],v))
                        return data[0][0]
                
        
    
    
    
    @classmethod
    def avg(cls,field,**kwargs):
        return cls.aggregate('AVG',field,**kwargs)

    @classmethod
    def min(cls,field,**kwargs):
        return cls.aggregate('MIN',field,**kwargs)
        
    @classmethod
    def max(cls,field,**kwargs):
        return cls.aggregate('MAX',field,**kwargs)
        
        
    @classmethod
    def sum(cls,field,**kwargs):
        return cls.aggregate('SUM',field,**kwargs)
        
    @classmethod
    def count(cls,field,**kwargs):
        return cls.aggregate('COUNT',field,**kwargs)

"""
            
