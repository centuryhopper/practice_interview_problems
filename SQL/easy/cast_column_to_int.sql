-- regex match for checking if stars
select cast(stars as int) stars, * from yelp_reviews
where stars ~ '^\d+$' and stars is not null

-- https://platform.stratascratch.com/coding/10056-cast-stars-column-values-to-integer-and-return-with-all-other-column-values?code_type=1

