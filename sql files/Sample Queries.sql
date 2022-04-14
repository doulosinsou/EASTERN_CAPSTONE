SELECT Post.title
FROM Post CROSS JOIN Post_cat ON Post.article_ID=Post_cat.article_ID CROSS JOIN Categories ON Post_cat.cat_name=Categories.cat_name
WHERE Categories.cat_status = "Subscription";

SELECT Post.title
FROM ((Post INNER JOIN Post_cat ON Post.article_ID=Post_cat.article_ID) INNER JOIN Categories ON Post_cat.cat_name=Categories.cat_name)
WHERE Categories.cat_status = "Public";

SELECT concat(Users.first_name, ' ', Users.last_name) AS author, Post.title, Post.subtitle
FROM ((Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID) INNER JOIN Users ON Writes.author_ID=Users.ID)
WHERE Users.last_name = "Moyer";

SELECT concat(Users.first_name, ' ', Users.last_name) AS Contributor, Post.title, Post.subtitle
FROM ((Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID) INNER JOIN Users ON Writes.author_ID=Users.ID);
