--------- Insert Default Data --------- 

--- Inserts for users ---

INSERT INTO Users (first_name, last_name, email, user_role, biography)
VALUES ('Lucas', 'Moyer', 'admin@moyeraudio.com','admin', 'Luke is the primary author of this project.');

INSERT INTO Users (first_name, last_name, email, user_role, biography)
VALUES ('Joe','Jerryfield','joejfield@website.com','author', 'Joe writes news articles');

INSERT INTO Users (first_name, last_name, email, user_role, biography)
VALUES ('Liz','Longerfield','lizlfield@website.com','author',"Liz writes children's articles");

INSERT INTO Users (first_name, last_name, email, user_role, biography)
VALUES ('Ashley','Atfield','ashleyafield@website.com','author',"Ashley writes science articles");


INSERT INTO Users (first_name, last_name, email, user_role, biography)
VALUES ('Abi','Andres','abiandres@website.com','contributor',"Abi edits news articles");

INSERT INTO Users (first_name, last_name, email, user_role, biography)
VALUES ('John','Jackson','johnjackson@website.com','contributor',"John edits science and children's articles");





--- Inserts for Page_type ---

INSERT INTO Page_type (type_name, template_link)
VALUES ('main','main.html');

INSERT INTO Page_type (type_name, template_link)
VALUES ('blog','blog.html');

INSERT INTO Page_type (type_name, template_link)
VALUES ('about','about.html');

INSERT INTO Page_type (type_name, template_link)
VALUES ('dashboard','dash.html');





--- Inserts for Theme --- 

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format)
VALUES ('Bright-wide', '#f7f9f8', '#fe0037', '1200px');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format)
VALUES ('Bright-medium', '#f7f9f8', '#fe0037', '900px');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format)
VALUES ('Bright-narrow', '#f7f9f8', '#fe0037', '600px');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format)
VALUES ('Dark-wide', '#323538', '#fe9815', '1200px');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format)
VALUES ('Dark-medium', '#323538', '#fe9815', '900px');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format)
VALUES ('Dark-narrow', '#323538', '#fe9815', '600px');




--- Inserts for Post --- 

INSERT INTO Post (title, page_type, content)
VALUES ('Home','main','<h1>Website Builder by Luke Moyer</h1><p>This Project creates a MySQL website database and serves it through Flask.</p><p>Follow the <a href="">Project</a> Category to read about the creation process.</p>');

INSERT INTO Post (title,subtitle, content)
VALUES ('Welcome','','<p>This Category will describe the creation process of this website builder</p>');

INSERT INTO Post (title,subtitle, content)
VALUES ('Public Lorem Ipsum','A static public category','<p>All posts are public</p>');

INSERT INTO Post (title,subtitle, content)
VALUES ('Subscribed Lorem Ipsum','A static subscription category','<p>All posts are viewable for subscribers</p>');

INSERT INTO Post (title,subtitle, content)
VALUES ('Premium Lorem Ipsum','A static premium category','<p>All posts are viewable for premium members</p>');




--- Inserts for Categories --- 

INSERT INTO Categories (cat_name, cat_status)
VALUES ('Project','public');

INSERT INTO Categories (cat_name, cat_status)
VALUES ('Public Blog','public');

INSERT INTO Categories (cat_name, cat_status)
VALUES ('Subscribed Blog','subscription');

INSERT INTO Categories (cat_name, cat_status)
VALUES ('Premium Blog','premium');



--- Inserts for Tags ---

INSERT INTO Tags (tag_name, article_ID)
VALUES ('webdesign',2);

INSERT INTO Tags (tag_name, article_ID)
VALUES ('database',2);

INSERT INTO Tags (tag_name, article_ID)
VALUES ('flask',2);

INSERT INTO Tags (tag_name, article_ID)
VALUES ('public',3);

INSERT INTO Tags (tag_name, article_ID)
VALUES ('subscription',4);

INSERT INTO Tags (tag_name, article_ID)
VALUES ('premium',5);



--- Inserts for Subscriber --- 

INSERT INTO Subscriber (email, sub_status)
VALUES ('basicSubscriber@subs.org', 'active');

INSERT INTO Subscriber (email, sub_status)
VALUES ('basicSubscriber2@subs.org', 'active');

INSERT INTO Subscriber (email, sub_status)
VALUES ('premiumSubscriber@subs.org', 'active');

INSERT INTO Subscriber (email, sub_status)
VALUES ('premiumSubscriber2@subs.org', 'active');



--- Inserts for Stats ---

INSERT INTO Stats (article_ID, IP_address)
VALUES (1,'123.123.123.123');

INSERT INTO Stats (article_ID, IP_address)
VALUES (1,'123.123.123.123');

INSERT INTO Stats (article_ID, IP_address)
VALUES (1,'456.456.456.456');

INSERT INTO Stats (article_ID, IP_address)
VALUES (2,'123.123.123.123');

INSERT INTO Stats (article_ID, IP_address)
VALUES (2,'456.456.456.456');

INSERT INTO Stats (article_ID, IP_address)
VALUES (3,'456.456.456.456');

INSERT INTO Stats (article_ID, IP_address)
VALUES (3,'789.789.789.789');



--- Inserts for Writes ---

INSERT INTO Writes (author_ID, article_ID)
VALUES (1,1);

INSERT INTO Writes (author_ID, article_ID)
VALUES (2,1);

INSERT INTO Writes (author_ID, article_ID)
VALUES (3,2);

INSERT INTO Writes (author_ID, article_ID)
VALUES (4,3);

INSERT INTO Writes (author_ID, article_ID)
VALUES (5,4);



--- Inserts for Post_cat ---

INSERT INTO Post_cat (cat_name, article_ID)
VALUES ('Project', 2);

INSERT INTO Post_cat (cat_name, article_ID)
VALUES ('Public Blog', 3);

INSERT INTO Post_cat (cat_name, article_ID)
VALUES ('Subscribed Blog', 4);

INSERT INTO Post_cat (cat_name, article_ID)
VALUES ('Premium Blog', 5);



--- Inserts for Contributes ---

INSERT INTO Contributes (contributor, article_ID)
VALUES (5, 3);

INSERT INTO Contributes (contributor, article_ID)
VALUES (6, 4);

INSERT INTO Contributes (contributor, article_ID)
VALUES (6, 5);



--- Inserts for Subscribes --- 

INSERT INTO Subscribes (sub_email, cat_name)
VALUES ("basicSubscriber@subs.org", "Project");

INSERT INTO Subscribes (sub_email, cat_name)
VALUES ("basicSubscriber2@subs.org", "Public Blog");

INSERT INTO Subscribes (sub_email, cat_name, membership)
VALUES ("basicSubscriber2@subs.org", "Subscribed Blog", 'Subscriber'); 

INSERT INTO Subscribes (sub_email, cat_name, membership)
VALUES ("premiumSubscriber@subs.org", "Premium Blog", "Premium"); 

INSERT INTO Subscribes (sub_email, cat_name, membership)
VALUES ("premiumSubscriber2@subs.org", "Project", "Premium"); 

INSERT INTO Subscribes (sub_email, cat_name, membership)
VALUES ("premiumSubscriber2@subs.org", "Public Blog", "Premium"); 

INSERT INTO Subscribes (sub_email, cat_name, membership)
VALUES ("premiumSubscriber2@subs.org", "Premium Blog", "Premium"); 




--- Inserts for Revenue ---

INSERT INTO Revenue (sub_email)
VALUES ('basicSubscriber@subs.org');

INSERT INTO Revenue (sub_email)
VALUES ('basicSubscriber2@subs.org');

INSERT INTO Revenue (sub_email, trans_amount)
VALUES ('premiumSubscriber@subs.org',20);

INSERT INTO Revenue (sub_email, trans_amount)
VALUES ('premiumSubscriber2@subs.org',20);

INSERT INTO Revenue (sub_email, trans_amount)
VALUES ('premiumSubscriber2@subs.org',20);