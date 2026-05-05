-- Lists all shows contained in 'hbtn_0d_tvshows'
-- that have at least one genre linked.

SELECT title, genre_id
FROM tv_shows
WHERE id in (SELECT DISTINCT show_id FROM tv_show_genres;)
JOIN tv_show_genres
ON id = show_id;