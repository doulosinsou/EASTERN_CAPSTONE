--- Equivalent Queries made from python def ---


--- def grab_article ---
SELECT Post.article_ID, Post.title, concat(Users.first_name,' ',Users.last_name) AS author, Post.subtitle, Post.post_date, Post.theme, Post.page_type, Post.post_order, Post.content, Post.cover_img_link
FROM Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID INNER JOIN Users ON Users.ID=Writes.author_ID
WHERE title="Welcome";

--- def grab_all_topics ---
SELECT topic_name, topic_status
FROM Topics;

--- def grab_articles_in_topic ---
SELECT Post.title
FROM Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name
WHERE Topics.topic_name="Project";

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
SELECT Post.title
FROM Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID
WHERE Users.ID=1;

--- def grab_contributor_articles ---
SELECT Post.title
FROM Post INNER JOIN Contributes ON Post.article_ID=Contributes.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID
WHERE Users.ID=5;


--- def grab_kin_article
SELECT Post.title, Topics.topic_name
FROM Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name
WHERE Topics.topic_name = "Project" AND Post.post_order = (SELECT post_order FROM Post WHERE title = "Project Goals") + 1 ;


--- def grab_subscribed_topics ---
SELECT Topics.topic_name
FROM Topics INNER JOIN Subscribes ON Topics.topic_name=Subscribes.topic_name INNER JOIN Subscriber ON Subscribes.sub_email=Subscriber.email
WHERE Subscriber.email = "basicSubscriber2@subs.org";


