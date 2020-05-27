Q1 = "SELECT fname,lname FROM Actor INNER JOIN Cast ON id==pid Where mid = 12148;"

Q2 = "SELECT COUNT(mid) FROM Cast INNER JOIN Actor ON pid==id WHERE fname = 'Harrison(I)' AND lname = 'Ford';"     

Q3 = "SELECT DISTINCT(pid) FROM Cast INNER JOIN Movie ON mid==id WHERE name like 'YoungLatinGirls%';"

Q4 = "SELECT COUNT(DISTINCT pid) FROM Cast INNER JOIN Movie ON mid == id WHERE year BETWEEN 1990 AND 2000;"

