select from_type, round(avg(review_score), 2) winner from airbnb_reviews
group by from_type
order by winner desc
limit 1

-- https://platform.stratascratch.com/coding/10072-guest-or-host-kindness?code_type=1
