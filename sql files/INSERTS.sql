--------- Insert Default Data --------- 

--- Inserts for users ---

INSERT INTO Users (first_name, last_name, email, user_role, biography, avatar_link)
VALUES ('Lucas', 'Moyer', 'admin@moyeraudio.com','admin', 'Luke is the primary author of this project.', 'man.png');

INSERT INTO Users (first_name, last_name, email, user_role, biography, avatar_link)
VALUES ('Joe','Jerryfield','joejfield@website.com','author', 'Joe writes news articles', 'man.png');

INSERT INTO Users (first_name, last_name, email, user_role, biography, avatar_link)
VALUES ('Liz','Longerfield','lizlfield@website.com','author',"Liz writes children's articles", 'woman.png');

INSERT INTO Users (first_name, last_name, email, user_role, biography, avatar_link)
VALUES ('Ashley','Atfield','ashleyafield@website.com','author',"Ashley writes science articles", 'woman.png');

INSERT INTO Users (first_name, last_name, email, user_role, biography, avatar_link)
VALUES ('Abi','Andres','abiandres@website.com','contributor',"Abi edits news articles", 'woman.png');

INSERT INTO Users (first_name, last_name, email, user_role, biography, avatar_link)
VALUES ('John','Jackson','johnjackson@website.com','contributor',"John edits science and children's articles", 'man.png');




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

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format, text_color)
VALUES ('Bright-wide', '#f7f9f8', '#fe0037', '1200px', '#5b5b5b');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format, text_color)
VALUES ('Bright-medium', '#f7f9f8', '#fe0037', '900px', '#5b5b5b');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format, text_color)
VALUES ('Bright-narrow', '#f7f9f8', '#fe0037', '600px', '#5b5b5b');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format, font)
VALUES ('Dark-wide', '#323538', '#fe9815', '1200px', 'Times');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format, font)
VALUES ('Dark-medium', '#323538', '#fe9815', '900px', 'Times');

INSERT INTO Theme (theme_name, color_primary, color_secondary, theme_format, font)
VALUES ('Dark-narrow', '#323538', '#fe9815', '600px', 'Times');




--- Inserts for Post --- 

INSERT INTO Post (title, page_type, content)
VALUES ('Home','main',"<h1>Website Builder by Luke Moyer</h1><p>This Project creates a MySQL website database and serves it through Flask.</p><p>Follow the <a href='/topic/Project_full'>Project_full</a> topic to read about the creation process.</p>
<p>Known bugs:</p>
<ol><li>The pages have inconsistent theme properties. This not a bug so much as randomized design to show that individual pages(posts) can have unique formatting</li>
<li>External links do not always render correctly. This is a Flask routing issue that needs further exploration. Typical answers include using url_for() or prepending https://. These are so far unsuccessful. I choose to leave them as-is for now and pursue an answer before production </li>
<li>Serving Images runs into problems. This is a Flask routing concern to research.</li>
<li>On the posts, there is a “Previous” and “Next” link to take a reader through the blog. There is an issue with Python's Mysql.connector rendering the request properly. From Workbench, the same query successfully provides the title which will take the reader to the next or previous page in the topic order. However, I cannot get the Python constructors to replicate this. I will need to find a solution or alternative before production. </li>
<li>On the Search page, using “enter” resets the page with a Get request. This is a matter of disabling the form action with javascript. I haven't had time to fix this.</li>
<li>On the Search page, the previews render raw html formatting. It would be good to insert a new 'Preview' Column to the Post table, to allow the author to manually type a raw text description or first sentences. This would be used for RSS feeds as well.</li>
<li>On the Dashboard, the KPI section does not adjust to parameters. This is due to the way the python sql function was built, and I did not have time to update it. The same is true for the Author's individual KPI's which use a view. I would need to recreate the view with the appropriate parameters. </li>
<li>On the Dashboard, the Author's engagement sparklines are individually scaled, and do not correspond to one another. </li>
<li>On the Dashboard, using the 'unique' filter sometimes does not appear to do anything. This is because the data is not quite as tailored for this. In a real-world production, the difference between unique visitors and return visitors is more obvious. </li>
<li>On the Project_full topic, some of the code blocks renterd with xml remove the tags, as they are interpreted literally in the HTML rendering.</li>
<li>On the Project_full topic, The TEMPLATES page distorts colors of the text, due to literal HTML rendering. Changing colors with developer tool is available. I will need to find a way to render the <pre>pre-code</pre> blocks as straight text..</li></ol>");

INSERT INTO Post (title,subtitle, content)
VALUES ('Welcome','','<p>This Category will describe the creation process of this website builder</p>');

INSERT INTO Post (title,subtitle, content)
VALUES ('Public Lorem Ipsum','A static public category','<p>All posts are public</p>');

INSERT INTO Post (title,subtitle, content)
VALUES ('Subscribed Lorem Ipsum','A static subscription category','<p>All posts are viewable for subscribers</p>');

INSERT INTO Post (title,subtitle, content)
VALUES ('Premium Lorem Ipsum','A static premium category','<p>All posts are viewable for premium members</p>');

INSERT INTO Post (title,subtitle, content, post_order)
VALUES ('Project Goals','Defining our purpose','<p>This is the second article in the Project topic</p>',1);

INSERT INTO Post (title,subtitle, content, post_order)
VALUES ('Data Handling','What is our project data?','<p>This is the third article in the Project topic</p>',2);



--- Inserts for Topics --- 

INSERT INTO Topics (topic_name, topic_status, topic_description)
VALUES ('Project','public','This topic regards the building and format of this website. This is a Capstone project in partial fulfillment of Eastern University\'s Data Science Master\'s program. This implementation is a MYSQL Database driven website. Follow the posts in this Topic to follow thie building stages and logic behind each step.');

INSERT INTO Topics (topic_name, topic_status,topic_description)
VALUES ('Public Blog','public','This topic represents all the blog posts that should be visible to the public. One does not have to subscribe in order to read these posts');

INSERT INTO Topics (topic_name, topic_status,topic_description)
VALUES ('Subscribed Blog','subscription','This topic represents all the blog posts that should be visible to basic subscribers. It would not be visible to the public without subscribeing. Anyone would be able to subscribe to this category free of charge');

INSERT INTO Topics (topic_name, topic_status,topic_description)
VALUES ('Premium Blog','premium','This topic represents all the blog posts that would only be visible to paid members (or promotional upgrades).');

INSERT INTO Topics (topic_name, topic_status,topic_description)
VALUES ('Uncategorized','public','This topic is a default backup for all posts which are otherwise unlabled.');




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
VALUES (1,2);

INSERT INTO Writes (author_ID, article_ID)
VALUES (2,3);

INSERT INTO Writes (author_ID, article_ID)
VALUES (3,4);

INSERT INTO Writes (author_ID, article_ID)
VALUES (4,5);

INSERT INTO Writes (author_ID, article_ID)
VALUES (1,6);

INSERT INTO Writes (author_ID, article_ID)
VALUES (1,7);



--- Inserts for Topic_Post ---

INSERT INTO Topic_Post (topic_name, article_ID)
VALUES ('Project', 2);

INSERT INTO Topic_Post (topic_name, article_ID)
VALUES ('Public Blog', 3);

INSERT INTO Topic_Post (topic_name, article_ID)
VALUES ('Subscribed Blog', 4);

INSERT INTO Topic_Post (topic_name, article_ID)
VALUES ('Premium Blog', 5);

INSERT INTO Topic_Post (topic_name, article_ID)
VALUES ('Project', 6);

INSERT INTO Topic_Post (topic_name, article_ID)
VALUES ('Project', 7);

INSERT INTO Topic_Post (topic_name, article_ID)
VALUES ('Uncategorized', 1);

INSERT INTO Topic_Post (topic_name, article_ID)
VALUES ('Public Blog', 1);



--- Inserts for Contributes ---

INSERT INTO Contributes (contributor, article_ID)
VALUES (5, 3);

INSERT INTO Contributes (contributor, article_ID)
VALUES (6, 4);

INSERT INTO Contributes (contributor, article_ID)
VALUES (6, 5);



--- Inserts for Subscribes --- 

INSERT INTO Subscribes (sub_email, topic_name)
VALUES ("basicSubscriber@subs.org", "Project");

INSERT INTO Subscribes (sub_email, topic_name)
VALUES ("basicSubscriber2@subs.org", "Public Blog");

INSERT INTO Subscribes (sub_email, topic_name, membership)
VALUES ("basicSubscriber2@subs.org", "Subscribed Blog", 'Subscriber'); 

INSERT INTO Subscribes (sub_email, topic_name, membership)
VALUES ("premiumSubscriber@subs.org", "Premium Blog", "Premium"); 

INSERT INTO Subscribes (sub_email, topic_name, membership)
VALUES ("premiumSubscriber2@subs.org", "Project", "Premium"); 

INSERT INTO Subscribes (sub_email, topic_name, membership)
VALUES ("premiumSubscriber2@subs.org", "Public Blog", "Premium"); 

INSERT INTO Subscribes (sub_email, topic_name, membership)
VALUES ("premiumSubscriber2@subs.org", "Premium Blog", "Premium"); 

INSERT INTO Subscribes (sub_email, topic_name, membership)
VALUES ("premiumSubscriber2@subs.org", "Subscribed Blog", "Premium"); 


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
