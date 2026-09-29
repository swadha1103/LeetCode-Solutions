# Write your MySQL query statement below
select name Customers
from Customers c left join Orders o
on c.id=o.customerID
where o.customerID is null;
