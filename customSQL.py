from tokenize import group
import mysql.connector
from auth import MYSQL_credentials as cred


class custom_SQL:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(**cred)
        except mysql.connector.Error as err:
            return(err)
    
    def select(self,Q,table,conditions=False,orderby=False,groupby=False):
        cur = self.con.cursor(buffered=True)
        statement = f'SELECT {Q} FROM {table}'
        if conditions:
            features = []
            matches = []
            for key in conditions:
                features.append(key)
                matches.append(conditions[key])

            statement += ' WHERE {}=%s'.format(features[0])
            if len(conditions.keys())>1:
                for feat in features[1:]:
                    statement += ' AND {}=%s'.format(feat)
            

            if orderby:
                statement+=" ORDER BY "+orderby
            if groupby:
                statement+=" GROUP BY "+groupby
            print(statement)
            cur.execute(statement,(*matches,))
        else:
            if orderby:
                statement+=" ORDER BY "+orderby
            if groupby:
                statement+=" GROUP BY "+groupby
            # cur.execute(statement,(Q,table))
            print(statement)
            cur.execute(statement)

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

    def insert(self,table,col_val_dict,close=True):
        cur = self.con.cursor(buffered=True)
        columns=tuple([key for key in col_val_dict.keys()])
        col_string=','.join(columns)
        values=tuple([col_val_dict[c] for c in columns])
        statement = 'INSERT INTO {} ({}) VALUES {}'.format(table,col_string,values)
        print(statement)
        
        # cur.execute(statement,(values,))
        cur.execute(statement)
        last_id = cur.lastrowid
        if close:
            cur.close()
            # self.commit()
        return last_id

    def exists(self,what,table,conditions):
        cur = self.con.cursor(buffered=True)
        statement = f'SELECT EXISTS( SELECT {what} FROM {table}'
        cond_keys = []
        cond_values = []
        for cond in conditions.keys():
            cond_keys.append(cond)
            cond_values.append(conditions[cond])
        statement += " WHERE {}=%s".format(cond_keys[0])
        if len(cond_keys)>1:
            for cond in cond_keys[1:]:
                statement += " AND {}=%s ".format(cond)
        statement += ")"
        vals = (*cond_values,)

        cur.execute(statement,vals)
        answer = cur.fetchone()
        return answer

    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()



########### SELECT ############

def grab_article(sql_obj, title, post_id=False):
    find="Post.article_ID, Post.title, concat(Users.first_name,' ',Users.last_name) AS author, Post.subtitle, Post.post_date, Post.theme, Post.page_type, Post.post_order, Post.content, Post.cover_img_link"
    table="Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID INNER JOIN Users ON Users.ID=Writes.author_ID"
    conditions={"Post.title":title}
    if post_id:
        conditions["Post.article_ID":post_id]
    return sql_obj.select(find,table,conditions)

def grab_all_topics(sql_obj):
    find="topic_name, topic_status"
    table="Topics"
    return sql_obj.select(find,table)

def grab_all_tags(sql_obj):
    find="tag_name, COUNT(*) as count"
    table="Tags GROUP BY tag_name ORDER BY count DESC"
    return sql_obj.select(find,table)

def grab_articles_in_topic(sql_obj,topic_name,order="DESC"):
    find="Post.title, Topics.topic_description, Topics.topic_status"
    table="Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name"
    conditions={"Topics.topic_name":topic_name}
    orderby=f"Post.post_order {order}, Post.post_date {order}"
    return sql_obj.select(find,table,conditions,orderby)

def grab_articles_in_tag(sql_obj,tag_name):
    find="Post.title, Topic_Post.topic_name"
    table=" Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Tags ON Post.article_ID=Tags.article_ID"
    conditions={"Tags.tag_name":tag_name}
    return sql_obj.select(find,table,conditions)

def grab_topics_in_article(sql_obj,article_ID):
    find="Topics.topic_name, Topics.topic_status"
    table="Topics INNER JOIN Topic_Post ON Topics.topic_name=Topic_Post.topic_name INNER JOIN Post ON Topic_Post.article_ID=Post.article_ID"
    conditions={"Post.article_ID":article_ID}
    return sql_obj.select(find,table,conditions)

def grab_tags_in_article(sql_obj,article_ID):
    find="tag_name"
    table="Tags"
    conditions={"article_ID":article_ID}
    return sql_obj.select(find,table,conditions)

def grab_authors(sql_obj):
    find="DISTINCT concat(Users.first_name,' ',Users.last_name) AS author, Users.avatar_link"
    table="Users INNER JOIN Writes ON Users.ID=Writes.author_ID"
    return sql_obj.select(find,table)

def grab_about_author(sql_obj,first_name,last_name):
    find="*,  DATE_FORMAT(date_employ, '%M %Y') as date, TIMESTAMPDIFF(DAY,date_employ,NOW()) as days_employed"
    table="Users"
    conditions={'first_name':first_name,'last_name':last_name}
    return sql_obj.select(find,table,conditions)

def grab_author_id(sql_obj,email):
    find="ID"
    table="Users"
    conditions={
        "email":email
    }
    return sql_obj.select(find,table,conditions)

def grab_contributors(sql_obj):
    find="DISTINCT concat(Users.first_name,' ',Users.last_name) AS contributor, Users.avatar_link"
    table="Users INNER JOIN Contributes ON Users.ID=Contributes.contributor"
    return sql_obj.select(find,table)

def grab_author_articles(sql_obj,author_ID):
    find="Post.title, Topic_Post.topic_name"
    table="(Post INNER JOIN Writes ON Post.article_ID=Writes.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID) INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID"
    conditions={"Users.ID":author_ID}
    orderby="topic_name"
    return sql_obj.select(find,table,conditions,orderby)

def grab_contributor_articles(sql_obj,contributor_ID):
    find="Post.title, Topic_Post.topic_name"
    table="(Post INNER JOIN Contributes ON Post.article_ID=Contributes.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID) INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID"
    conditions={"Users.ID":contributor_ID}
    orderby="topic_name"
    return sql_obj.select(find,table,conditions,orderby)

def grab_kin_article(sql_obj,title,topic,kin):
    find="Post.title,Topics.topic_name"
    table="Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID INNER JOIN Topics ON Topic_Post.topic_name=Topics.topic_name"
    conditions={
        "Topics.topic_name":topic,
        "Post.post_order":f'((SELECT post_order FROM Post WHERE title = "{title}") + {kin})'
        }
    print(find, '/n', table, '/n', conditions)
    return sql_obj.select(find,table,conditions)

def grab_subscribed_topics(sql_obj,user_email):
    find="Topics.topic_name"
    table="Topics INNER JOIN Subscribes ON Topics.topic_name=Subscribes.topic_name INNER JOIN Subscriber ON Subscribes.sub_email=Subscriber.email"
    conditions={"Subscriber.email":user_email}
    return sql_obj.select(find,table,conditions)

def grab_public_topics(sql_obj):
    find="topic_name"
    table="Topics"
    conditions={"topic_status":"public"}
    return sql_obj.select(find,table,conditions)

def grab_role(sql_obj,email):
    find="role"
    table="(SELECT email, user_role AS role FROM Users UNION SELECT sub_email, membership AS role FROM Subscribes) AS all_users"
    conditions={"email":email}
    return sql_obj.select(find,table,conditions)

def grab_article_feed(sql_obj,email):
    find="Topics.topic_name, Topics.topic_status, Subscribes.membership, Post.article_ID, Post.title, Post.post_date"
    table="(Topics INNER JOIN Subscribes ON Topics.topic_name=Subscribes.topic_name INNER JOIN Subscriber ON Subscribes.sub_email=Subscriber.email) INNER JOIN (Post INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID) ON Topics.topic_name=Topic_Post.topic_name"
    conditions={"Subscriber.email":email,"Subscriber.sub_status":"active"}
    orderby="Post.post_date DESC LIMIT 10"
    return sql_obj.select(find,table,conditions,orderby)

def grab_theme(sql_obj,theme):
    find="*"
    table="Theme"
    conditions={"theme_name":theme}
    return sql_obj.select(find,table,conditions)





############# INSERTS ##############

def put_article(sql_obj,title,subtitle,theme,content,post_order):
    table = 'Post'
    col_value= {
        'title':title,
        'subtitle':subtitle,
        'content':content,
        'post_order':post_order,
        'theme':theme
    }
    return sql_obj.insert(table,col_value)

def put_topic(sql_obj,name,status,description):
    table = 'Topics'
    col_value= {
        'topic_name':name,
        'topic_status':status,
        'topic_description':description
    }
    return sql_obj.insert(table,col_value)
    
def put_tag(sql_obj,name,article_ID):
    table = 'Tags'
    col_value= {
        'tag_name':name,
        'article_ID':article_ID,
    }
    return sql_obj.insert(table,col_value)

def put_stat(sql_obj,article_ID,IP_address,datetime):
    table = 'Stats'
    col_value= {
        'IP_address':IP_address,
        'article_ID':article_ID,
        'visit':datetime
    }
    return sql_obj.insert(table,col_value)

def put_writes(sql_obj,article_ID,author_ID):
    table = 'Writes'
    col_value= {
        'author_ID':author_ID,
        'article_ID':article_ID,
    }
    return sql_obj.insert(table,col_value)

def put_topic_post(sql_obj,topic_name,article_ID):
    table = 'Topic_Post'
    col_value= {
        'topic_name':topic_name,
        'article_ID':article_ID,
    }
    return sql_obj.insert(table,col_value)

def put_contributes(sql_obj,article_ID,contributor_ID):
    table = 'Contributes'
    col_value= {
        'contributor':contributor_ID,
        'article_ID':article_ID,
    }
    return sql_obj.insert(table,col_value)


def put_revenue(sql_obj,email,amount):
    table = 'Revenue'
    col_value= {
        'sub_email':email,
        'trans_amount':amount,
    }
    return sql_obj.insert(table,col_value)