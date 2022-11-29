select worker_title from worker
join title on worker.worker_id = title.worker_ref_id
group by worker_title
order by sum(salary) desc
limit 2

-- https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?tabname=discussion