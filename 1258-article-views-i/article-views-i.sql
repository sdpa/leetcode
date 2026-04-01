# Write your MySQL query statement below


select distinct Views.author_id as id
from Views
where Views.viewer_id = Views.author_id
order by id asc