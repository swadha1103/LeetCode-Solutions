# Write your MySQL query statement below
select name,population,area as "area"
from World
where population>=25000000 or area >=3000000;