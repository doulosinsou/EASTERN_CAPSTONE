
--- def kpi_av_day_views_in_month ---

SELECT ROUND( AVG(c.views) ,2) as av
FROM (SELECT COUNT(IP_address) as views
	FROM Stats 
    WHERE YEAR(visit) ='2020' and MONTH(visit)='4'
    GROUP BY MONTH(visit), DAY(visit)) as c;


 --- def kpi_revenue_goal_month ---
 
 SELECT (SUM(trans_amount)/4500 * 100) as percent_goal
 FROM Revenue
 WHERE YEAR(trans_date)='2022' and MONTH(trans_date)='4';


--------- Count of views per site,article,topic,tag,author,contributor ---------

--- def stat_site_views ---
SELECT COUNT(IP_address) as all_views
FROM Stats;

--- def stat_site_unique_viewers ---
SELECT COUNT(DISTINCT IP_address) as unique_viewers
FROM Stats;

--- def stat_article_views ---
SELECT COUNT(IP_address) as all_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID
WHERE Post.title = 'Home';

--- def stat_article_unique_viewers ---
SELECT COUNT(DISTINCT IP_address) as unique_viewers
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID
WHERE Post.title = 'Home';

--- def stat_views_site_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day
FROM Stats
GROUP BY year, month, day, hour, SECOND(visit);

--- def stat_unique_views_site_time ---
SELECT COUNT(DISTINCT IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats
GROUP BY year, month, day, hour, SECOND(visit);

--- def stat_views_article_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID
WHERE Post.title = 'Home'
GROUP BY year, month, day, hour, SECOND(visit);

--- def stat_unique_views_article_time ---
SELECT COUNT(DISTINCT IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID
WHERE Post.title = 'Home'
GROUP BY year, month, day, hour, SECOND(visit);

--- def stat_all_topic_views ---
SELECT COUNT(IP_address) as all_views, Topic_Post.topic_name
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID
GROUP BY Topic_Post.topic_name;



--- def stat_all_topic_views_time ---
SELECT COUNT(IP_address) as count_, Topic_Post.topic_name as cat_, YEAR(visit) as year, MONTH(visit) as month
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID
GROUP BY cat_, year, month;




--- def stat_topic_views ---
SELECT COUNT(IP_address) as all_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID
WHERE Topic_Post.topic_name = 'Public Blog';

SELECT COUNT(DISTINCT IP_address) as unique_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID
WHERE Topic_Post.topic_name = 'Public Blog';

--- def stat_topic_views_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID
WHERE Topic_Post.topic_name = 'Public Blog'
GROUP BY year, month, day, hour, SECOND(visit);

--- def stat_all_tag_views ---
SELECT COUNT(IP_address) as all_views, Tags.tag_name
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Tags ON Post.article_ID=Tags.article_ID
GROUP BY Tags.tag_name;


--- def stat_all_tag_subs_time---
SELECT COUNT(DISTINCT sub_email) as count_, Tags.tag_name as cat_, YEAR(sub_date) as year, MONTH(sub_date) as month
FROM (Subscribes INNER JOIN Topic_Post ON Subscribes.topic_name=Topic_Post.topic_name) INNER JOIN Tags ON Topic_Post.article_ID=Tags.article_ID
GROUP BY cat_, year, month;




--- def stat_tag_views ---
SELECT COUNT(IP_address) as all_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Tags ON Post.article_ID=Tags.article_ID
WHERE Tags.tag_name = 'demo';

--- def stat_tag_views_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Tags ON Post.article_ID=Tags.article_ID
WHERE Tags.tag_name = 'demo'
GROUP BY year, month, day, hour;

--- def stat_author_views ---
SELECT COUNT(IP_address) as all_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer";

SELECT COUNT(DISTINCT IP_address) as all_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer";

--- def stat_author_views_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer"
GROUP BY year, month, day, hour, SECOND(visit);


--- def stat_author_topic_views ---
SELECT COUNT(IP_address) as all_views, Topic_Post.topic_name
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer"
GROUP BY topic_name;

--- def stat_author_topic_views_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer" AND Topic_Post.topic_name='Project'
GROUP BY year, month, day, hour;

--- def stat_all_author_posts ---
SELECT COUNT(article_ID) AS post, CONCAT(first_name,' ',last_name) as author
FROM Writes INNER JOIN Users ON Writes.author_id=Users.ID
GROUP BY author;







--- def stat_all_author_posts_revenue ---
-- EXAMPLE --

--- What are the total posts per author and what is that authors revenue contribution? 
--- Authors contribution defined as: the sum of reveue associated with subscribers who subscribe to topics to which the author also contributes


SELECT post,revenue, post_count.author, post_count.avatar_link
FROM
(SELECT COUNT(article_ID) AS post, CONCAT(first_name,' ',last_name) as author, Users.avatar_link
FROM Writes INNER JOIN Users ON Writes.author_id=Users.ID
GROUP BY author ) as post_count
INNER JOIN
(SELECT SUM(trans_amount) AS revenue, author
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author
		FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name INNER JOIN Revenue ON Subscribes.sub_email=Revenue.sub_email
GROUP BY author) as author_revenue
ON post_count.author=author_revenue.author;

--- Equivalent to below view ---

SELECT * FROM author_stats;



--- def stat_contributor_views ---
SELECT COUNT(IP_address) as all_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Contributes ON Contributes.article_ID=Post.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer";

--- def stat_contributor_views_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Contributes ON Contributes.article_ID=Post.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer"
GROUP BY year, month, day, hour, SECOND(visit);

--- def stat_contributor_topic_views ---
SELECT COUNT(IP_address) as all_views, Topic_Post.topic_name
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Contributes ON Contributes.article_ID=Post.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer"
GROUP BY topic_name;

--- def stat_contributor_topic_views_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Contributes ON Contributes.article_ID=Post.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID
WHERE Users.first_name = 'Lucas' AND Users.last_name = "Moyer" AND Topic_Post.topic_name='Project'
GROUP BY year, month, day, hour;






--------- Count of subscriptions per site,article,topic,author,contributor ---------



--- def stat_site_subs ---
SELECT COUNT(sub_email) AS count_subs 
FROM Subscribes;

--- def stat_site_subs_time ---
SELECT COUNT(sub_email) AS count_subs, sub_date, YEAR(sub_date) as year, MONTH(sub_date) as month, DAY(sub_date) AS day
FROM Subscribes
GROUP BY year, month;

--- def stat_all_topic_subs ---
SELECT COUNT(Subscribes.sub_email) AS count_subs, Subscribes.topic_name
FROM Subscribes INNER JOIN Topics ON Subscribes.topic_name=Topics.topic_name
GROUP BY Subscribes.topic_name;


--- def stat_all_topic_subs_time ---
SELECT COUNT(Subscribes.sub_email) AS count_subs, Subscribes.topic_name, YEAR(sub_date) as year, MONTH(sub_date) as month
FROM Subscribes INNER JOIN Topics ON Subscribes.topic_name=Topics.topic_name
WHERE YEAR(sub_date) = 2020 and MONTH(sub_date) = 4
GROUP BY Subscribes.topic_name, year, month;


--- def stat_topic_subs
SELECT COUNT(sub_email) AS count_subs 
FROM Subscribes
WHERE topic_name='Premium Blog';

--- def stat_membership_subs ---
SELECT COUNT(sub_email) AS count_subs, membership
FROM Subscribes
GROUP BY membership;

--- def stat_all_author_subs ---
SELECT COUNT(author) AS count_subs, author
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author
		FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name
GROUP BY author;


--- def stat_all_author_subs_time ---
SELECT COUNT(author) AS viewers, author, YEAR(sub_date) as year, MONTH(sub_date) as month, DAY(sub_date) as day
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author
		FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name
GROUP BY author;





--- def stat_author_subs ---
SELECT COUNT(author) AS count_subs, author
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author 
		FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name
WHERE author='Lucas Moyer';



--- def stat_author_subs_time ---
SELECT COUNT(sub_email) AS viewers, author, YEAR(sub_date) as year, MONTH(sub_date) as month, DAY(sub_date) as day
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author 
		FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name
WHERE author='Lucas Moyer'
GROUP BY year, month, day;




--- def stat_all_contributor_subs ---
SELECT COUNT(author) AS count_subs, author
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author
		FROM Users INNER JOIN Contributes ON Users.ID=Contributes.contributor INNER JOIN Topic_Post ON Contributes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name
GROUP BY author;

--- def stat_contributor_subs ---
SELECT COUNT(author) AS count_subs, author
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author
		FROM Users INNER JOIN Contributes ON Users.ID=Contributes.contributor INNER JOIN Topic_Post ON Contributes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name
WHERE author = 'Lucas Moyer';







--------- SUM of revenue per site,article,topic,author,contributor ---------




--- def stat_site_revenue ---
SELECT SUM(trans_amount)
FROM Revenue;

--- def stat_all_topics_revenue ---
SELECT SUM(trans_amount), Topics.topic_name
FROM Revenue INNER JOIN Subscribes ON Revenue.sub_email=Subscribes.sub_email INNER JOIN Topics ON Subscribes.topic_name=Topics.topic_name
GROUP BY Topics.topic_name;

--- def stat_topic_revenue ---
SELECT SUM(trans_amount), Topics.topic_name
FROM Revenue INNER JOIN Subscribes ON Revenue.sub_email=Subscribes.sub_email INNER JOIN Topics ON Subscribes.topic_name=Topics.topic_name
WHERE Topics.topic_name='Project';

--- def stat_author_revenue ---
SELECT SUM(trans_amount) AS revenue, author
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author
		FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name INNER JOIN Revenue ON Subscribes.sub_email=Revenue.sub_email
GROUP BY author;

