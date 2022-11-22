select city, property_type, avg(bathrooms) as n_bathrooms_avg, avg(bedrooms) as n_bedrooms_avg from airbnb_search_details
group by city, property_type

-- https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?code_type=1