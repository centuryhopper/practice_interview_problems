select artist, Count(artist) as n_occurrences
from spotify_worldwide_daily_song_ranking
-- cannot group by aggregate functions, so thats why we dont have:
-- group by artist, n_occurrences
group by artist
order by n_occurrences desc

-- https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=1

