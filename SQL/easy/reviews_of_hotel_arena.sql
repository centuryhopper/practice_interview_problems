select hotel_name, reviewer_score, count(*) count
from hotel_reviews
where hotel_name = 'Hotel Arena'
group by hotel_name, reviewer_score



-- https://platform.stratascratch.com/coding/10166-reviews-of-hotel-arena?code_type=1
