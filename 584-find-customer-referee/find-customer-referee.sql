-- Write your PostgreSQL query statement below
select c.name from customer as c
where c.referee_id is null or  referee_id != 2 

