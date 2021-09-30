/* Write your T-SQL query statement below */
select Customers.name as Customers 
from Customers left join Orders
on Customers.Id = Orders.CustomerId
where Orders.CustomerId is null
