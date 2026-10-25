# Write your MySQL query statement below
select machine_id,
round(avg(process_time),3) as processing_time
from(
    select machine_id,process_id,
    max(case when activity_type='end' then timestamp end) -max(case when activity_type='start' then timestamp end) as process_time
    from Activity
    group by machine_id,process_id )as t
group by machine_id