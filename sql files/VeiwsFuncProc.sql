--- CREATING A VIEW ---

CREATE VIEW author_stats AS
SELECT post,revenue, post_count.author, post_count.avatar_link
FROM
	(SELECT COUNT(Writes.article_ID) AS post, CONCAT(first_name,' ',last_name) as author, Users.avatar_link
	FROM Writes INNER JOIN Users ON Writes.author_id=Users.ID
	GROUP BY author ) as post_count
INNER JOIN
	(SELECT SUM(trans_amount) AS revenue, author
	FROM 	(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author
			FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID
			GROUP BY author, topic_name) AS U 
	INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name INNER JOIN Revenue ON Subscribes.sub_email=Revenue.sub_email
	GROUP BY author) as author_revenue
ON post_count.author=author_revenue.author;







--- Create Functions ---

-- This function returns the subscription eligibility based on current subscription status OR one year aniversaries of subscription date
-- For use in the def grab_role query

DELIMITER $$

CREATE FUNCTION SubscriptionLevel(membership varchar(12), sub_date datetime)
RETURNS varchar(12)
DETERMINISTIC
BEGIN
	DECLARE new_membership varchar(12);
    
    IF membership='Premium' 
		THEN SET new_membership = membership;
    ELSEIF (YEAR(sub_date) < YEAR(NOW()) AND MONTH(sub_date)=MONTH(NOW()) ) 
		THEN SET new_membership='Premium';
	ELSE SET new_membership=membership;
	END IF;
    
    RETURN (new_membership);

END$$
DELIMITER ;


