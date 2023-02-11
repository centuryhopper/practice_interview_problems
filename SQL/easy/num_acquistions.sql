select acquired_quarter, count(*) cnt_acq from crunchbase_acquisitions
group by acquired_quarter
order by cnt_acq desc

-- https://platform.stratascratch.com/coding/10162-number-of-acquisitions?code_type=1
