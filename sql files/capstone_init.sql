--- Creating the Database ---

-- DROP DATABASE Capstone; --
-- CREATE DATABASE	 Capstone; --

-- SET FOREIGN_KEY_CHECKS = 0;
-- DROP TABLE Categories;
-- DROP TABLE Contributes;
-- DROP TABLE Page_type;
-- DROP TABLE Post;
-- DROP TABLE Post_cat;
-- DROP TABLE Revenue;
-- DROP TABLE Stats;
-- DROP TABLE Subscriber;
-- DROP TABLE Subscribes;
-- DROP TABLE Tags;
-- DROP TABLE Theme;
-- DROP TABLE Users;
-- DROP TABLE Writes;
-- 


--- Creating the Entity tables ---


CREATE TABLE Users (
	ID			SMALLINT NOT NULL AUTO_INCREMENT,
	first_name	char(20) DEFAULT '',
    last_name	char(20) NOT NULL,
	date_employ TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    email		varchar(50) NOT NULL UNIQUE,
    user_role	char(12) CHECK (user_role in ('admin','author','contributor')),
    biography 	MEDIUMTEXT,
    avatar_link	varchar(100) DEFAULT 'default_avatar.png',
    
    CONSTRAINT Users_pk PRIMARY KEY (ID)
);

CREATE TABLE Page_type (
	type_name		char(20) NOT NULL UNIQUE,
    template_link 	varchar(100) DEFAULT 'main.html',
    
    CONSTRAINT Page_type_pk PRIMARY KEY (type_name)
);

CREATE TABLE Theme (
	theme_ID		SMALLINT NOT NULL AUTO_INCREMENT,
    theme_name		varchar(20) NOT NULL UNIQUE,
    color_primary	varchar(20) DEFAULT '#f7f9f8',
    color_secondary	varchar(20) DEFAULT '#fe0037',
    text_color		varchar(20) DEFAULT '#5b5b5b',
    theme_format	varchar(12) DEFAULT '900px' CHECK(theme_format in ('600px','900px','1200px')),
    font			varchar(12) DEFAULT 'Arial',
    
    CONSTRAINT theme_pk PRIMARY KEY (theme_ID)
);

CREATE TABLE Post (
	article_ID	SMALLINT NOT NULL AUTO_INCREMENT,
	title		varchar(50) NOT NULL,
    subtitle	char(100),
	post_date 	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    theme		varchar(20) DEFAULT 'Bright-medium',
    page_type	char(20) DEFAULT 'blog',
    post_order	SMALLINT DEFAULT 0,
    content 	LONGTEXT,
    cover_img_link	varchar(100),
    
    CONSTRAINT Post_pk PRIMARY KEY (article_ID),
	CONSTRAINT Post_page_fk FOREIGN KEY (page_type) REFERENCES Page_type (type_name),
    CONSTRAINT Post_theme_fk FOREIGN KEY (theme) REFERENCES Theme (theme_name)
);

CREATE TABLE Topics (
	topic_name		varchar(20) NOT NULL UNIQUE,
    topic_status	varchar(12) DEFAULT 'public' CHECK(topic_status in ('public','premium','subscription')),
    topic_description	LONGTEXT,
    
    CONSTRAINT Categories_pk PRIMARY KEY (topic_name)
);

CREATE TABLE Tags (
	tag_name	varchar(20) NOT NULL,
    article_ID	SMALLINT NOT NULL,
    
    CONSTRAINT Tags_pk PRIMARY KEY (tag_name, article_ID),
    CONSTRAINT Tags_fk FOREIGN KEY (article_ID) REFERENCES Post (article_ID)
);

CREATE TABLE Subscriber (
	email	varchar(50) NOT NULL,
    sub_status	varchar(12) DEFAULT 'active' CHECK(sub_status in ('active','inactive')),
    
    CONSTRAINT Subscriber_pk PRIMARY KEY (email)
);

CREATE TABLE Stats (
	article_ID 	SMALLINT NOT Null,
    IP_address 	varchar(50),
    visit		DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT Stats_pk PRIMARY KEY (article_ID,IP_address,visit),
    CONSTRAINT Stats_fk FOREIGN KEY (article_ID) REFERENCES Post (article_ID)
);



--- Creating the Relationship tables ---


CREATE TABLE Writes (
	author_ID	SMALLINT NOT NULL,
    article_ID	SMALLINT NOT NULL,
    updated		DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    CONSTRAINT Writes_pk PRIMARY KEY (author_ID, article_ID),
    CONSTRAINT Writes_auth_fk FOREIGN KEY (author_ID) REFERENCES Users (ID),
    CONSTRAINT Writes_art_fk FOREIGN KEY (article_ID) REFERENCES Post (article_ID)
);

CREATE TABLE Topic_Post (
	topic_name	varchar(20) DEFAULT 'Uncategorized',
    article_ID	SMALLINT NOT NULL,
    
    CONSTRAINT Topic_Post_pk PRIMARY KEY (topic_name, article_ID),
    CONSTRAINT Topic_Post_topic_fk FOREIGN KEY (topic_name) REFERENCES Topics (topic_name),
    CONSTRAINT Topic_Post_art_fk FOREIGN KEY (article_ID) REFERENCES Post (article_ID)
);

CREATE TABLE Contributes (
	contributor	SMALLINT NOT NULL,
    article_ID	SMALLINT NOT NULL,
    
    CONSTRAINT Contrubutes_pk PRIMARY KEY (contributor, article_ID),
    CONSTRAINT Contributes_cont_fk FOREIGN KEY (contributor) REFERENCES Users (ID),
    CONSTRAINT Contributes_art_fk FOREIGN KEY (article_ID) REFERENCES Post (article_ID)
);

CREATE TABLE Subscribes (
	sub_email 	varchar(50) NOT NULL,
    topic_name	varchar(20) NOT NULL,
    membership	varchar(12) DEFAULT 'Subscriber' CHECK(membership in ('Premium','Subscriber')),
    sub_date	DATETIME DEFAULT CURRENT_TIMESTAMP,
    renewed_date	DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    CONSTRAINT Subscribes_pk PRIMARY KEY (sub_email, topic_name),
    CONSTRAINT Subscribes_email_fk FOREIGN KEY (sub_email) REFERENCES Subscriber (email),
    CONSTRAINT Subscribes_topic_fk FOREIGN KEY (topic_name) REFERENCES Topics (topic_name)
);

CREATE TABLE Revenue (
	sub_email 		varchar(50) NOT NULL,
    trans_date		DATETIME DEFAULT CURRENT_TIMESTAMP,
    trans_amount	SMALLINT DEFAULT 10,
    
    CONSTRAINT Revenue_pk PRIMARY KEY (sub_email, trans_date),
    CONSTRAINT Revenue_email_fk FOREIGN KEY (sub_email) REFERENCES Subscriber (email)
);


