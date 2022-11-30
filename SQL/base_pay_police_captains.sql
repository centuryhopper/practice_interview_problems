select employeename, SUM(basepay) from sf_public_salaries
where jobtitle = 'CAPTAIN III (POLICE DEPARTMENT)'
group by employeename

-- https://platform.stratascratch.com/coding/9972-find-the-base-pay-for-police-captains?code_type=1