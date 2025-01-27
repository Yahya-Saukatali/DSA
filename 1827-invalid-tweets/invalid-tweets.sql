-- Write your PostgreSQL query statement below
select t.tweet_id from tweets as t
where length(content) > 15