--- Creating the Database ---

-- DROP DATABASE Capstone; --
-- CREATE DATABASE	 Capstone; --

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
    template_link 	varchar(100) DEFAULT 'default_template.png',
    
    CONSTRAINT Page_type_pk PRIMARY KEY (type_name)
);

CREATE TABLE Theme (
	theme_ID		SMALLINT NOT NULL AUTO_INCREMENT,
    theme_name		varchar(20) NOT NULL UNIQUE,
    color_primary	varchar(20),
    color_secondary	varchar(20),
    theme_format	varchar(12) DEFAULT '900px' CHECK(theme_format in ('600px','900px','1200px')),
    font			varchar(12) DEFAULT 'Arial',
    
    CONSTRAINT theme_pk PRIMARY KEY (theme_ID)
);

CREATE TABLE Post (
	article_ID	SMALLINT NOT NULL AUTO_INCREMENT,
	title		varchar(50) NOT NULL,
    subtitle	char(100),
	post_date 	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    theme		varchar(20) DEFAULT 'Dark-wide',
    page_type	char(20) DEFAULT 'blog',
    post_order	SMALLINT DEFAULT 0,
    content 	LONGTEXT,
    cover_img_link	varchar(100),
    
    CONSTRAINT Post_pk PRIMARY KEY (article_ID),
	CONSTRAINT Post_page_fk FOREIGN KEY (page_type) REFERENCES Page_type (type_name),
    CONSTRAINT Post_theme_fk FOREIGN KEY (theme) REFERENCES Theme (theme_name)
);

CREATE TABLE Categories (
	cat_name	varchar(20) NOT NULL UNIQUE,
    cat_status	varchar(12) DEFAULT 'public' CHECK(cat_status in ('public','premium','subscription')),
    
    CONSTRAINT Categories_pk PRIMARY KEY (cat_name)
);

CREATE TABLE Tags (
	tag_name	varchar(20) NOT NULL,
    article_ID	SMALLINT NOT NULL,
    
    CONSTRAINT Tags_pk PRIMARY KEY (tag_name, article_ID),
    CONSTRAINT Tags_fk FOREIGN KEY (article_ID) REFERENCES Post (article_ID)
);

CREATE TABLE Subscriber (
	email	varchar(50) NOT NULL,
    sub_status	varchar(12) DEFAULT 'inactive' CHECK(sub_status in ('active','inactive')),
    
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

CREATE TABLE Post_cat (
	cat_name	varchar(20) DEFAULT 'Uncategorized',
    article_ID	SMALLINT NOT NULL,
    
    CONSTRAINT Post_cat_pk PRIMARY KEY (cat_name, article_ID),
    CONSTRAINT Post_cat_cat_fk FOREIGN KEY (cat_name) REFERENCES Categories (cat_name),
    CONSTRAINT Post_cat_art_fk FOREIGN KEY (article_ID) REFERENCES Post (article_ID)
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
    cat_name	varchar(20) NOT NULL,
    membership	varchar(12) DEFAULT 'subscriber' CHECK(membership in ('premium','subscriber')),
    sub_date	DATETIME DEFAULT CURRENT_TIMESTAMP,
    renewed_date	DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    CONSTRAINT Subscribes_pk PRIMARY KEY (sub_email, cat_name),
    CONSTRAINT Subscribes_email_fk FOREIGN KEY (sub_email) REFERENCES Subscriber (email),
    CONSTRAINT Subscribes_cat_fk FOREIGN KEY (cat_name) REFERENCES Categories (cat_name)
);

CREATE TABLE Revenue (
	sub_email 		varchar(50) NOT NULL,
    trans_date		DATETIME DEFAULT CURRENT_TIMESTAMP,
    trans_amount	SMALLINT DEFAULT 0,
    
    CONSTRAINT Revenue_pk PRIMARY KEY (sub_email, trans_date),
    CONSTRAINT Revenue_email_fk FOREIGN KEY (sub_email) REFERENCES Subscriber (email)
);
