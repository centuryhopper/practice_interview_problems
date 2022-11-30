
-- old hacky subquery way of doing it
-- select union_sum.date, total_energy from
-- (
--     select date, sum(consumption) as summ from
--     (
--         select * from fb_eu_energy
--         union all
--         select * from fb_asia_energy
--         union all
--         select * from fb_na_energy
--     ) as unioned
--     group by date
-- ) as union_sum
-- inner join
-- (
--     select max(summ) as total_energy from
--     (
--         select date, sum(consumption) as summ from
--         (
--             select * from fb_eu_energy
--             union all
--             select * from fb_asia_energy
--             union all
--             select * from fb_na_energy
--         ) as unioned
--         group by date
--     ) as final
-- ) as main on main.total_energy = union_sum.summ

-- my improved solution using WITH CLAUSE
with

union_sum (date, total_energy) as
(
    select date, sum(consumption) as summ from
    (
        select * from fb_eu_energy
        union all
        select * from fb_asia_energy
        union all
        select * from fb_na_energy
    ) as unioned
    group by date
),

max_energy (max_energy) as
(
    select max(total_energy) from
    union_sum
)

select date,total_energy from union_sum
inner join max_energy on total_energy = max_energy

-- find the max value and join it with the summed table
-- https://platform.stratascratch.com/coding/10064-highest-energy-consumption?tabname=resources






