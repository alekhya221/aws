Q1 = "SELECT COUNT(ID) AS count FROM Movie WHERE year < 2000;"

Q2 = "SELECT AVG(rank) AS average_rank FROM Movie WHERE year == 1991;"                          

Q3 = "SELECT MIN(rank) AS min_rank FROM Movie WHERE year == 1991;"

Q4 = "SELECT fname,lname FROM Actor INNER JOIN Cast ON id == pid WHERE mid == 27;"

Q5 = "SELECT COUNT(DISTINCT mid) FROM Cast INNER JOIN Actor ON pid == id WHERE fname == 'Jon' AND lname == 'Dough';"                                  

Q6 = "SELECT name FROM Movie WHERE (name like 'Young Latin Girls%') AND (year BETWEEN 2003 AND 2006);"    

Q7 = "SELECT fname,lname FROM ((Director INNER JOIN MovieDirector ON Director.id=MovieDirector.did)INNER JOIN Movie ON Movie.id=MovieDirector.mid) WHERE Movie.name  like 'Star Trek%';"                             

Q8 = "SELECT name FROM  ((((Movie INNER JOIN MovieDirector ON `Movie`.id='MovieDirector'.mid) INNER JOIN Director ON 'Director'.id= 'MovieDirector'.did) INNER JOIN Cast ON 'Movie'.id='Cast'.mid)INNER JOIN Actor ON 'Actor'.id = 'Cast'.pid) WHERE 'Director'.fname='Jackie (I)' AND 'Director'.lname='Chan' AND 'Actor'.fname='Jackie (I)' AND 'Actor'.lname='Chan' ;"         


Q9 = "SELECT fname,lname FROM ((Director INNER JOIN MovieDirector ON Director.id=MovieDirector.did)INNER JOIN Movie ON Movie.id=MovieDirector.mid) WHERE Movie.year = 2001 GROUP BY Director.id HAVING COUNT(Director.id) >=4 ORDER BY Director.fname ASC,Director.lname DESC;"

Q10 = "SELECT gender,COUNT(id) FROM Actor WHERE gender = 'F' UNION SELECT gender,count(id) FROM Actor WHERE gender = 'M';"

Q11 = '''SELECT DISTINCT 'Movie1'.name, 'Movie2'.name, 'Movie1'.rank, 'Movie1'.year
         FROM Movie AS Movie1 JOIN Movie AS Movie2
         ON 'Movie2'.rank = 'Movie1'.rank AND 'Movie2'.name != 'Movie1'.name AND 'Movie2'.year = 'Movie1'.year
         ORDER BY 'Movie1'.name ASC
         LIMIT 100;'''
         
Q12 = '''SELECT 'Actor'.fname, 'Movie'.year, AVG(rank) AS rank
         FROM ((Actor JOIN Cast ON 'Actor'.id = pid) JOIN Movie ON `Movie`.id = mid)
         GROUP BY 'Movie'.year, 'Actor'.id
         ORDER BY 'Actor'.fname ASC, 'Movie'.year DESC
         LIMIT 100;'''
         
Q13 = '''SELECT 'Actor'.fname, 'Director'.fname, AVG(rank) AS score
         FROM ((((Movie JOIN Cast ON 'Movie'.id = 'Cast'.mid) JOIN MovieDirector ON 'MovieDirector'.did = 'Movie'.id) JOIN Actor ON 'Actor'.id = 'Cast'.pid) JOIN Director ON 'Director'.id = 'MovieDirector'.did)
         GROUP BY 'Actor'.id, 'Director'.id
         HAVING COUNT('MovieDirector'.mid) >= 5
         ORDER BY score DESC, 'Director'.fname ASC, 'Actor'.fname DESC
         LIMIT 100;'''











    





















































"""
Q11 = '''SELECT DISTINCT `Movie1`.name, `Movie2`.name, `Movie1`.rank, `Movie1`.year
         FROM Movie AS Movie1 JOIN Movie AS Movie2
         ON `Movie2`.rank = `Movie1`.rank AND `Movie2`.name != `Movie1`.name AND `Movie2`.year = `Movie1`.year
         ORDER BY `Movie1`.name ASC
         LIMIT 100;'''
         
Q12 = '''SELECT `Actor`.fname, `Movie`.year, AVG(rank) AS rank
         FROM ((Actor JOIN Cast ON `Actor`.id = pid) JOIN Movie ON `Movie`.id = mid)
         GROUP BY `Movie`.year, `Actor`.id
         ORDER BY `Actor`.fname ASC, `Movie`.year DESC
         LIMIT 100;'''
         
Q13 = '''SELECT `Actor`.fname, `Director`.fname, AVG(rank) AS score
         FROM ((((Movie JOIN Cast ON `Movie`.id = `Cast`.mid) JOIN MovieDirector ON `MovieDirector`.mid  = `Movie`.id) JOIN Actor ON `Actor`.id = `Cast`.pid) JOIN Director ON `Director`.id = `MovieDirector`.did)
         GROUP BY `Actor`.id, `Director`.id
         HAVING COUNT(`MovieDirector`.mid) >= 5
         ORDER BY score DESC, `Director`.fname ASC, `Actor`.fname DESC
         LIMIT 100;'''
"""         



























"""Q11 = '''SELECT DISTINCT `Movie1`.name, `Movie2`.name, `Movie1`.rank, `Movie1`.year
         FROM Movie AS Movie1 JOIN Movie AS Movie2
         ON `Movie2`.rank = `Movie1`.rank AND `Movie2`.name != `Movie1`.name AND `Movie2`.year = `Movie1`.year
         ORDER BY `Movie1`.name ASC
         LIMIT 100;'''
         
Q12 = '''SELECT `Actor`.fname, `Movie`.year, AVG(rank) AS rank
         FROM ((Actor JOIN Cast ON `Actor`.id = pid) JOIN Movie ON `Movie`.id = mid)
         GROUP BY `Movie`.year, `Actor`.id
         ORDER BY `Actor`.fname ASC, `Movie`.year DESC
         LIMIT 100;'''
         
Q13 = '''SELECT `Actor`.fname, `Director`.fname, AVG(rank) AS score
         FROM ((((Movie JOIN Cast ON `Movie`.id = `Cast`.mid) JOIN MovieDirector ON `MovieDirector`.mid  = `Movie`.id) JOIN Actor ON `Actor`.id = `Cast`.pid) JOIN Director ON `Director`.id = `MovieDirector`.did)
         GROUP BY `Actor`.id, `Director`.id
         HAVING COUNT(`MovieDirector`.mid) >= 5
         ORDER BY score DESC, `Director`.fname ASC, `Actor`.fname DESC
         LIMIT 100;'''  
         
"""