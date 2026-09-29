# Write your MySQL query statement below
select Department,Employee,Salary
from(select d1.name as Department,
e1.name as Employee,
e1.salary as Salary,
dense_rank() over
(partition by d1.name order by salary desc)as rnk
from Employee e1 inner join Department d1
on e1.departmentID=d1.id) as tmp
where rnk<=3