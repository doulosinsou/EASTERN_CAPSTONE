--- Views ---

CREATE VIEW About AS
	SELECT first_name, last_name, user_role, biography, updated as 'Last active', title 
    FROM Users, Post, Writes
    WHERE Writes.author_ID = Users.ID and Writes.article_ID = Post.article_ID
    
;    