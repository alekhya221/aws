Q1 ="SELECT d.id, d.fname FROM Director as d WHERE EXISTS (SELECT m.id FROM Movie as m INNER JOIN MovieDirector as md ON m.id=md.mid WHERE d.id=md.did AND m.year>2000) AND NOT EXISTS (SELECT m.id FROM Movie as m INNER JOIN MovieDirector as md ON m.id = md.mid WHERE d.id=md.did AND m.year<2000) ORDER BY id ASC;"                                                      
                                           
#Q2 = "SELECT name,max(rank) from Movie,Director,MovieDirector where id=mid id =did and director.id=31"

Q2 = "SELECT fname,(SELECT name from Movie,Director,MovieDirector where Movie.id=mid and Director.id =did and director.id=d.id ORDER BY rank DESC) FROM Director as d;"

Q3 = "SELECT * FROM Actor WHERE NOT EXISTS (SELECT mid FROM Movie  INNER JOIN Cast  ON Movie.id = Cast.mid WHERE m.year between 1990 and 2000);"






"""@property
    def name(self):
        return self._name
    @property    
    def age(self):
        return self._age
        
    @property
    def score(self):
        return self._score
"""
