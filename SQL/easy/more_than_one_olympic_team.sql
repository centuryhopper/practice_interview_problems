select name, team, games, sport, medal from olympics_athletes_events
where team ilike '%/%'
group by name, team, games, sport, medal

-- https://platform.stratascratch.com/coding/10143-find-players-who-participated-in-the-olympics-representing-more-than-one-team?code_type=1
