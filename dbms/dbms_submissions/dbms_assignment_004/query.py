Q1 = "SELECT COUNT(ID) FROM Movie WHERE (year = 2002) AND (name like 'Ha%' AND rank > 2)"

Q2 = "SELECT MAX(rank) FROM Movie WHERE (name like 'Autom%') AND (year = 1983 OR year = 1994)" 

Q3 = "SELECT COUNT(ID) FROM Actor WHERE (gender = 'M') AND (fname like '%ei' OR lname like 'ei%')"

Q4 = "SELECT AVG(rank) AS average_rank_of_movies FROM Movie WHERE (year == 1993 OR year == 1995 OR year == 2000) AND (rank >= 4.2)"   

Q5 = "SELECT SUM(rank) FROM Movie WHERE (name like '%Hary%') AND(year BETWEEN 1981 AND 1984) AND (rank < 9)"

Q6 = "SELECT MIN(year) FROM Movie WHERE rank = 5"

Q7 = "SELECT COUNT(ID) FROM Actor WHERE (gender == 'F') OR (fname == lname)"

Q8 = "SELECT DISTINCT fname FROM Actor WHERE lname like '%ei' ORDER BY fname ASC LIMIT 100"

Q9 = "SELECT id,name AS movie_title,year FROM Movie WHERE year IN(2001,2002,2005,2006) LIMIT 25 OFFSET 10"

Q10 = "SELECT DISTINCT lname FROM Director WHERE fname IN('Yeud','Wolf','Vicky') ORDER BY lname ASC LIMIT 5"


Q11 = "SELECT d.id FROM Director d WHERE "




SELECT d.id, d.fname,
FROM Director d 
WHERE EXISTS (
    SELECT m.id 
    FROM Movie as m INNER JOIN MovieDirector as md ON m.id=md.mid
    WHERE d.id=md.did AND m.year>2000
) AND NOT EXISTS (
    SELECT m.id 
    FROM Movie as m INNER JOIN MovieDirector as md ON m.id = md.mid
    WHERE d.id=md.did AND m.year<2000
);

