select business_name, stars, count(review_id) n_reviews from yelp_reviews
where business_name = 'Lo-Lo''s Chicken & Waffles'
group by stars, business_name
order by stars

-- https://platform.stratascratch.com/coding/10058-find-the-number-of-reviews-received-by-lo-los-chicken-waffles-for-each-star?tabname=solutions

