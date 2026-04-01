# Write your MySQL query statement below

select Tweets.tweet_id
from Tweets
where LENGTH(Tweets.content) > 15
