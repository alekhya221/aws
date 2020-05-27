Q1 = "SELECT AVG(age) FROM Player;"

Q2 = "SELECT match_no,play_date FROM Match WHERE audience > 50000;"

Q3 = "SELECT team_id,COUNT(win_lose) as no_of_matches FROM MatchTeamDetails WHERE win_lose == 'W' GROUP BY team_id ORDER BY COUNT(win_lose) DESC;"                                                                                                               

Q4 = "SELECT match_no,play_date FROM Match WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match) ORDER BY match_no DESC ;"

Q5 = "SELECT 'matchcaptain'.match_no,'team'.name as team_name,'player'.name as captain_name FROM ((Team INNER JOIN Player ON 'team'.team_id = 'player'.team_id) INNER JOIN MatchCaptain ON 'team'.team_id='matchcaptain'.team_id) WHERE 'player'.player_id = 'matchcaptain'.captain ORDER BY 'matchcaptain'.match_no,'team'.name ASC;"                                                                                                           


Q6 = "SELECT  match_no,name,jersey_no FROM Match JOIN Player ON player_id = player_of_match ORDER BY match_no ASC;"

Q7 = "SELECT 'team'.name as name,avg('player'.age) as average_age FROM (TEAM INNER JOIN PLAYER ON 'team'.team_id = 'player'.team_id) GROUP BY 'team'.team_id  HAVING avg('player'.age) > 26 ORDER BY 'team'.name ;"

Q8 = "SELECT 'player'.name,'player'.jersey_no,'player'.age,count('goaldetails'.goal_id)as no_of_goals FROM (Player INNER JOIN GoalDetails ON 'player'.player_id = 'goaldetails'.player_id)WHERE age<= 27 GROUP BY 'player'.player_id ORDER BY no_of_goals DESC,'player'.name ASC;"


Q9 ="SELECT team_id,COUNT(goal_id)*100.0/(SELECT COUNT(goal_id)FROM GoalDetails)FROM GoalDetails GROUP BY team_id Having COUNT(goal_id) <> 0;"

Q10 ="SELECT AVG(no_of_goals) AS avg_no_of_goals FROM (SELECT COUNT(goal_id) AS no_of_goals FROM GoalDetails GROUP BY team_id);"


#Q11 = "SELECT 'player'.player_id,'player'.name,'player'.date_of_birth FROM Player INNER JOIN Team ON 'player'.team_id = 'team'.team_id INNER JOIN MatchTeamDetails ON 'matchteamdetails'.team_id = 'team'.team_id WHERE 'matchteamdetails'.goal_score =0 GROUP BY 'player'.player_id ORDER BY 'player'.player_id;"





Q11 = "SELECT player_id,name,date_of_birth FROM Player as p WHERE NOT EXISTS (SELECT goal_id FROM GoalDetails WHERE 'GoalDetails'.player_id=p.player_id)ORDER BY player_id ASC;"

Q12 = '''SELECT `T`.name, `M`.match_no, audience AS audience, audience - (SELECT AVG(audience) FROM Match JOIN MatchTeamDetails ON `Match`.match_no = `MatchTeamDetails`.match_no AND T.team_id = `MatchTeamDetails`.team_id)
         FROM MatchTeamDetails JOIN Match AS M ON `MatchTeamDetails`.match_no = `M`.match_no
         JOIN Team AS T ON `MatchTeamDetails`.team_id = `T`.team_id
         ORDER BY `M`.match_no ASC;'''

































"""Q1='''SELECT AVG(AGE) FROM PLAYER;'''

Q2='''SELECT MATCH_NO,PLAY_DATE FROM MATCH WHERE AUDIENCE>50000 ORDER BY MATCH_NO;'''

Q4='''SELECT MATCH_NO,PLAY_DATE FROM MATCH WHERE STOP1_SEC>(SELECT AVG(STOP1_SEC) FROM MATCH) ORDER BY MATCH_NO DESC;'''

Q5='''SELECT `MATCHCAPTAIN`.MATCH_NO,`TEAM`.NAME,`PLAYER`.NAME FROM TEAM INNER JOIN MATCHCAPTAIN ON `TEAM`.TEAM_ID=`MATCHCAPTAIN`.TEAM_ID INNER JOIN PLAYER ON `MATCHCAPTAIN`.CAPTAIN=`PLAYER`.PLAYER_ID ORDER BY `MATCHCAPTAIN`.MATCH_NO,`TEAM`.NAME ASC;'''

Q6='''SELECT DISTINCT `MATCHCAPTAIN`.MATCH_NO,`PLAYER`.NAME AS PLAYER_OF_MATCH,JERSEY_NO FROM MATCHCAPTAIN INNER JOIN PLAYER ON `MATCHCAPTAIN`.CAPTAIN=`PLAYER`.PLAYER_ID INNER JOIN MATCH ON `MATCH`.PLAYER_OF_MATCH=`PLAYER`.PLAYER_ID ORDER BY `MATCHCAPTAIN`.MATCH_NO;'''

Q7='''SELECT `TEAM`.NAME,AVG(AGE) AS AVG_AGE FROM TEAM INNER JOIN PLAYER ON `TEAM`.TEAM_ID=`PLAYER`.TEAM_ID GROUP BY `TEAM`.NAME HAVING AVG(AGE)>26 ORDER BY `TEAM`.NAME;'''

Q8='''SELECT `PLAYER`.NAME,JERSEY_NO,AGE,COUNT(GOAL_ID) AS NUMBER_OF_GOALS FROM PLAYER INNER JOIN GOALDETAILS ON `PLAYER`.PLAYER_ID=`GOALDETAILS`.PLAYER_ID WHERE AGE<=27 GROUP BY `GOALDETAILS`.PLAYER_ID ORDER BY NUMBER_OF_GOALS DESC,`PLAYER`.NAME ASC;'''

Q9='''SELECT `TEAM`.TEAM_ID,(COUNT(GOAL_ID)*100/(SELECT COUNT(GOAL_ID) FROM GOALDETAILS)) FROM TEAM INNER JOIN GOALDETAILS ON `TEAM`.TEAM_ID=`GOALDETAILS`.TEAM_ID GROUP BY `GOALDETAILS`.TEAM_ID;'''

Q10='''SELECT AVG(NUMBER_OF_GOALS) FROM (SELECT COUNT(GOAL_ID) AS NUMBER_OF_GOALS FROM GOALDETAILS GROUP BY TEAM_ID);'''

Q11='''SELECT `PLAYER`.PLAYER_ID,`PLAYER`.NAME,`PLAYER`.DATE_OF_BIRTH FROM PLAYER INNER JOIN TEAM ON `PLAYER`.TEAM_ID=`TEAM`.TEAM_ID INNER JOIN MATCHTEAMDETAILS ON `TEAM`.TEAM_ID=`MATCHTEAMDETAILS`.TEAM_ID WHERE GOAL_SCORE=0 GROUP BY `PLAYER`.PLAYER_ID ORDER BY `PLAYER`.PLAYER_ID;'''
"""