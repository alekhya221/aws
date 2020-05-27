Q1 = "select 'actor'.id,'actor'.fname,'actor'.lname,'actor'.gender from actor inner join cast on 'actor'.id = 'cast'.pid inner join movie on 'cast'.mid='movie'.id where 'movie'.name like 'Annie%';"                                                                                                                            

Q2 = "select 'movie'.id,'movie'.name,'movie'.rank,'movie'.year from movie inner join moviedirector on 'movie'.id = 'moviedirector'.mid inner join director on 'moviedirector'.did='director'.id where ('director'.fname='Biff' and 'director'.lname='Malibu') and 'movie'.year in (1999,1994,2003) order by 'movie'.rank desc,'movie'.year asc;"

Q3 = "select year,count(id) as no_of_movies from movie   group by year having avg(rank)> (select avg(rank) from movie) order by year asc;"

Q4 = "select id,name,year,rank from movie where rank < (select avg(rank) from movie) and year in (2001) order by rank desc limit 10;"

Q6 = "select distinct 'cast'.pid from actor inner join cast on 'actor'.id='cast'.pid inner join movie on 'movie'.id = 'cast'.mid group by 'actor'.id,'movie'.id having count(distinct 'cast'.role) > 1 order by 'actor'.id asc limit 100;"

Q7 = "select fname,count(fname) as count from director group by fname having count(fname) > 1;"


Q8 ="select d.id,d.fname,d.lname from director d where exists(select c.pid from cast c inner join moviedirector md on md.mid = c.mid where md.did=d.id group by md.mid having count(distinct c.pid) >=100) and not exists(select pid from cast c inner join moviedirector md on c.mid = md.mid where d.id = md.did group by md.mid having count(distinct c.pid) < 100);"                                            

