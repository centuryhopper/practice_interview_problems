
select business_type, sum(adwords_earnings) earnings from google_adwords_earnings
group by business_type;

-- https://platform.stratascratch.com/coding/10164-total-adwords-earnings?code_type=1
