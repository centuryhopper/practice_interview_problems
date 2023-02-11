select gender, count(*) n_appointments from medical_appointments
group by gender
order by n_appointments desc
limit 1

-- https://platform.stratascratch.com/coding/10170-gender-with-most-doctor-appointments?tabname=solutions