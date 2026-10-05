# Write your MySQL query statement below

select distinct s.name
from SalesPerson s left join Orders o
on s.sales_id=o.sales_id left join Company c
on o.com_id=c.com_id
where s.sales_id not in (select o.sales_id
                    from SalesPerson s left join Orders o
                    on s.sales_id=o.sales_id left join Company c
                    on o.com_id=c.com_id
                    where o.com_id in  (select c.com_id
                                        from SalesPerson s left join Orders o
                                        on s.sales_id=o.sales_id left join Company c
                                        on o.com_id=c.com_id
                                        where c.name ='RED'));


   



