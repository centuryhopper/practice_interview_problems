select distinct facebook_posts.post_id, facebook_posts.poster, facebook_posts.post_text, facebook_posts.post_keywords, facebook_posts.post_date from facebook_posts
INNER JOIN facebook_reactions on facebook_posts.post_id = facebook_reactions.post_id
where reaction = 'heart'

-- https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?tabname=discussion

-- my comments: I like the wildcard way of selecting from the facebook_posts table

-- official solution:
-- SELECT
--     distinct
--     p.*
-- FROM
--     facebook_posts p
-- INNER JOIN
--     facebook_reactions r
-- ON
--     p.post_id = r.post_id AND
--     r.reaction = 'heart'
