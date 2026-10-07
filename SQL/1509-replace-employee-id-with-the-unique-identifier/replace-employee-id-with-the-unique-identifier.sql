# Write your MySQL query statement below
select unique_id ,
    case 
        when e.id=eu.id then e.name
        else e.name
    end as name
    
from Employees e left join EmployeeUNI eu
on e.id=eu.id
