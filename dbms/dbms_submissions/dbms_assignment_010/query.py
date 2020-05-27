Q1 = "select mc.captain,mc.team_id,p.jersey_no,p.name,p.date_of_birth,p.age from player p inner join matchcaptain mc on mc.captain=p.player_id where exists(select captain from matchcaptain where p.player_id = mc.captain) and not exists (select gd.goal_id from goaldetails gd where p.player_id=gd.player_id);"
 
Q2 = "select team_id,count(match_no) from matchteamdetails group by team_id;"

Q3 = "select team_id,(count(goal_id)/23.0) as avg_goal_score from goaldetails group by team_id;"

Q4 = "select captain,count(match_no) as no_of_times_captain from matchcaptain group by captain;"

Q5 = "select count(distinct player.player_id) as no_players from match inner join player on match.player_of_match=player.player_id inner join matchcaptain on matchcaptain.captain=player.player_id where matchcaptain.captain =player.player_id and player.player_id=match.player_of_match and matchcaptain.match_no = match.match_no;"        

Q6 = "select distinct captain from matchcaptain inner join player on matchcaptain.captain=player.player_id and player.player_id not in(select player_of_match from match);"

Q7 = "select distinct strftime('%m',play_date) as m,count(match_no) from match group by m;"
 
Q8= "select jersey_no,count(captain) as no_captains from player inner join matchcaptain on matchcaptain.captain = player.player_id group by jersey_no order by no_captains desc,jersey_no desc;"

Q9 = "select p.player_id,avg(m.audience) as avg_audience from player p inner join matchteamdetails mt on  mt.team_id=p.team_id inner join match m on mt.match_no = m.match_no  group by p.player_id order by avg_audience desc,p.player_id desc;"


Q10 = "select team_id,avg(age) from player group by team_id;"

Q11 = "select avg(age) as avg_age_of_captains from player inner join matchcaptain on captain=player_id;"

Q12 = "select strftime('%m',date_of_birth) as m,count(player_id) as no_of_players from player group by m order by no_of_players desc,m desc;"

Q13 = "select captain,count(win_lose) as no_of_wins from matchcaptain mc inner join matchteamdetails mt on mc.team_id= mt.team_id and mc.match_no=mt.match_no where win_lose = 'W' group by captain order by no_of_wins desc;"