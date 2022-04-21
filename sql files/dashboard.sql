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
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
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

--- def stat_topic_views ---
SELECT COUNT(IP_address) as all_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID
WHERE Topic_Post.topic_name = 'Public Blog';

SELECT COUNT(DISTINCT IP_address) as all_views
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID
WHERE Topic_Post.topic_name = 'Public Blog';

--- def stat_topic_views_time ---
SELECT COUNT(IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour
FROM Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID
WHERE Topic_Post.topic_name = 'Public Blog'
GROUP BY year, month, day, hour, SECOND(visit);


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

--- def stat_site_subs ---
SELECT COUNT(sub_email) AS count_subs 
FROM Subscribes;

--- def stat_all_topic_subs ---
SELECT COUNT(Subscribes.sub_email) AS count_subs, Subscribes.topic_name
FROM Subscribes INNER JOIN Topics ON Subscribes.topic_name=Topics.topic_name
GROUP BY Subscribes.topic_name;

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

--- def stat_author_subs ---
SELECT COUNT(author) AS count_subs, author
FROM (SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author
		FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID
		GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name
WHERE author='Lucas Moyer';

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


