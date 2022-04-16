import mysql.connector
from auth import MYSQL_credentials as cred


class custom_SQL:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(**cred)
        except mysql.connector.Error as err:
            return(err)
    
    def select(self,Q,table,conditions,where=False):
        cur = self.con.cursor(buffered=True)
        statement = f'SELECT {Q} FROM {table}'
        if where:
            features = []
            matches = []
            for key in conditions:
                features.append(key)
                matches.append(conditions[key])

            statement += ' WHERE {}=%s'.format(features[0])
            if len(conditions.keys())>1:
                for feat in features[1:]:
                    statement += ' AND {}=%s'.format(feat)
            # print(statement)
            cur.execute(statement,(*matches,))
        else:
            cur.execute(statement,(Q,table))

        column_names = [c[0] for c in cur.description]
        data_dict = dict()
        for name in column_names:
            data_dict[name] = []
        results = [cur.fetchall()]
        for row in results[0]:
            for i, col in enumerate(row):
                data_dict[column_names[i]].append(col)
        cur.close()

        return data_dict

    def insert(self,table,columns,values,close=True):
        cur = self.con.cursor(buffered=True)
        statement = 'INSERT INTO %s %s VALUES %s'
        cur.execute(statement,(table,columns,values))
        last_id = cur.lastrowid
        if close:
            cur.close()
        return last_id


    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()



def grab_article(sql_obj, title, post_id=False):
    find="Post.article_ID, Post.title, concat(Users.first_name,' ',Users.last_name) AS author, Post.subtitle, Post.post_date, Post.theme, Post.page_type, Post.post_order, Post.content, Post.cover_img_link"
    table="Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID INNER JOIN Users ON Users.ID=Writes.author_ID"
    conditions={"Post.title":title}
    if post_id:
        conditions["Post.article_ID":post_id]
    return sql_obj.select(find,table,conditions,where=True)

def grab_all_topics(sql_obj):
    find="topic_name, topic_status"
    table="Topics"
    return sql_obj.select(find,table)

def grab_articles_in_topic(sql_obj,topic_name):
    find="Post.title"
    table="Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name"
    conditions={"Topics.topic_name":topic_name}
    return sql_obj.select(find,table,conditions,where=True)

def grab_topics_in_article(sql_obj,article_ID):
    find="Topics.topic_name"
    table="Topics INNER JOIN Topic_Post ON Topics.topic_name=Topic_Post.topic_name INNER JOIN Post ON Topic_Post.article_ID=Post.article_ID"
    conditions={"Post.article_ID":article_ID}
    return sql_obj.select(find,table,conditions,where=True)

def grab_tags_in_article(sql_obj,article_ID):
    find="tag_name"
    table="Tags"
    conditions={"article_ID":article_ID}
    return sql_obj.select(find,table,conditions,where=True)

def grab_authors(sql_obj):
    find="DISTINCT concat(Users.first_name,' ',Users.last_name) AS author"
    table="Users INNER JOIN Writes ON Users.ID=Writes.author_ID"
    return sql_obj.select(find,table)

def grab_contributors(sql_obj):
    find="DISTINCT concat(Users.first_name,' ',Users.last_name) AS contributor"
    table="Users INNER JOIN Contributes ON Users.ID=Contributes.author_ID"
    return sql_obj.select(find,table)

def grab_author_articles(sql_obj,author_ID):
    find="Post.title"
    table="Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID"
    conditions={"Users.ID":author_ID}
    return sql_obj.select(find,table,conditions,where=True)

def grab_contributor_articles(sql_obj,contributor_ID):
    find="Post.title"
    table="Post INNER JOIN Contributes ON Post.article_ID=Contributes.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID"
    conditions={"Users.ID":contributor_ID}
    return sql_obj.select(find,table,conditions,where=True)

def grab_kin_article(sql_obj,title,topic,kin):
    find="Post.title,Topics.topic_name"
    table="Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name"
    conditions={
        "Topics.topic_name":topic,
        "Post.post_order":f'(SELECT post_order FROM Post WHERE title = "{title}") + {kin}'
        }
    print(find, '/n', table, '/n', conditions)
    return sql_obj.select(find,table,conditions,where=True)

def grab_subscribed_topics(sql_obj,user_email):
    find="Topics.topic_name"
    table="Topics INNER JOIN Subscribes ON Topics.topic_name=Subscribes.topic_name INNER JOIN Subscriber ON Subscribes.sub_email=Subscriber.email"
    conditions={"Subscriber.email":user_email}
    return sql_obj.select(find,table,conditions,where=True)

def grab_public_topics(sql_obj):
    find="topic_name"
    table="Topics"
    conditions={"topic_status":"public"}
    return sql_obj.select(find,table,conditions,where=True)

def grab_role(sql_obj,email):
    find="role"
    table="(SELECT email, user_role AS role FROM Users UNION SELECT sub_email, membership AS role FROM Subscribes) AS all_users"
    conditions={"email":email}
    return sql_obj.select(find,table,conditions,where=True)





