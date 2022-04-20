--- Equivalent Queries made from python def ---


--- def grab_article ---
SELECT Post.article_ID, Post.title, concat(Users.first_name,' ',Users.last_name) AS author, Post.subtitle, Post.post_date, Post.theme, Post.page_type, Post.post_order, Post.content, Post.cover_img_link
FROM Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID INNER JOIN Users ON Users.ID=Writes.author_ID
WHERE title="Welcome";

--- def grab_all_topics ---
SELECT topic_name, topic_status
FROM Topics;

--- def grab_articles_in_topic_newst_first ---
SELECT Post.title
FROM Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name
WHERE Topics.topic_name="Project"
ORDER BY Post.post_order DESC, Post.post_date DESC;

--- def grab_articles_for_topic_oldest_first ---
SELECT Post.title
FROM Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name
WHERE Topics.topic_name="Project"
ORDER BY Post.post_order ASC, Post.post_date ASC;

--- def grab_articles_in_tag---
SELECT Post.title, Topic_Post.topic_name
FROM Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Tags ON Post.article_ID=Tags.article_ID
WHERE Tags.tag_name="public";

--- def grab_all_tags ---
SELECT tag_name, COUNT(*) as count
FROM Tags
GROUP BY tag_name
ORDER BY count DESC;

--- def grab_topics_in_article ---
SELECT Topics.topic_name
FROM Topics INNER JOIN Topic_Post ON Topics.topic_name=Topic_Post.topic_name INNER JOIN Post ON Topic_Post.article_ID=Post.article_ID
WHERE Post.article_ID=1;

--- def grab_authors ---
SELECT DISTINCT concat(Users.first_name, ' ', Users.last_name) AS author, ID
FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID;

--- def grab_contributors ---
SELECT DISTINCT concat(Users.first_name, ' ', Users.last_name) AS contributor, ID
FROM Users INNER JOIN Contributes ON Users.ID=Contributes.contributor;

--- def grab_author_articles ---
SELECT Post.title, Topic_Post.topic_name
FROM (Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID) INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID
WHERE Users.ID=1
ORDER BY topic_name;


--- def grab_contributor_articles ---
SELECT Post.title
FROM Post INNER JOIN Contributes ON Post.article_ID=Contributes.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID
WHERE Users.ID=5;

--- def grab_about_author ---
SELECT *, DATE_FORMAT(date_employ, '%M %Y') as date, TIMESTAMPDIFF(DAY,date_employ,NOW()) as days_employed
FROM Users
WHERE first_name="Lucas" AND last_name="Moyer";

--- def grab_kin_article ---
SELECT Post.title, Topics.topic_name
FROM Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name
WHERE Topics.topic_name = "Project" AND Post.post_order = ((SELECT post_order FROM Post WHERE title = "Project Goals" LIMIT 1) + 1) ;

SELECT post_order FROM Post WHERE title = "Public Lorem Ipsum 3" LIMIT 1;

--- def grab_subscribed_topics ---
SELECT Topics.topic_name
FROM Topics INNER JOIN Subscribes ON Topics.topic_name=Subscribes.topic_name INNER JOIN Subscriber ON Subscribes.sub_email=Subscriber.email
WHERE Subscriber.email = "basicSubscriber2@subs.org";

--- def grab_public_topics ---
SELECT topic_name 
FROM Topics
WHERE topic_status="public";

--- def grab_role ---
SELECT role 
FROM (SELECT email, user_role AS role
	FROM Users
		UNION
	SELECT sub_email, membership AS role
	FROM Subscribes) AS all_users
WHERE email="basicSubscriber@subs.org";

--- def grab_article_feed ---
SELECT Topics.topic_name, Topics.topic_status, Subscribes.membership, Post.article_ID, Post.title, Post.post_date
FROM 	(Topics INNER JOIN Subscribes ON Topics.topic_name=Subscribes.topic_name INNER JOIN Subscriber ON Subscribes.sub_email=Subscriber.email) 
	INNER JOIN 
		(Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID) 
	ON Topics.topic_name=Topic_Post.topic_name
WHERE Subscriber.email = "premiumSubscriber2@subs.org" AND Subscriber.sub_status="active"
ORDER BY Post.post_date DESC;


--- def grab_theme ---
SELECT *
FROM Theme
WHERE theme_name="Dark-wide";

--- method exists ---

SELECT EXISTS(
	SELECT membership
    FROM Subscribes
    WHERE sub_email='basicSubscriber@subs.org' AND topic_name='Premium Blog'
);


SELECT * FROM Post 
WHERE content LIKE '%Purpose%';