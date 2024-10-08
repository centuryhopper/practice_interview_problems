
-- official stratascratch solution (not mine)
SELECT DISTINCT(a1.user_id)
FROM amazon_transactions a1
JOIN amazon_transactions a2 ON a1.user_id=a2.user_id
AND a1.id != a2.id
AND a2.created_at::date-a1.created_at::date BETWEEN 0 AND 7
ORDER BY a1.user_id

-- https://platform.stratascratch.com/coding/10322-finding-user-purchases?tabname=discussion