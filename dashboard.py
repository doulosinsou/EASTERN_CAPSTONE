from datetime import datetime

import customSQL
from customSQL import custom_SQL

def stat_site_views(sql_obj, unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers"
    table="Stats"
    return sql_obj.select(find,table)

def stat_article_views(sql_obj,post_title,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID"
    conditions={'Post.title':post_title}
    return sql_obj.select(find,table,conditions=conditions)

def stat_views_site_time(sql_obj,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour"
    table="Stats"
    group="year, month, day, hour"
    return sql_obj.select(find,table,groupby=group)

def stat_views_article_time(sql_obj,post_title,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID"
    conditions={'Post.title':post_title}
    group="year, month, day, hour"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_all_topic_views(sql_obj,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID"
    group='Topic_Post.topic_name'
    return sql_obj.select(find,table,groupby=group)

def stat_topic_views(sql_obj,topic_name,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID"
    conditions={'Topic_Post.topic_name':topic_name}
    return sql_obj.select(find,table,conditions=conditions)

def stat_views_topic_time(sql_obj,topic_name,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Topic_Post ON Post.article_ID=Topic_Post.article_ID"
    conditions={'Topic_Post.topic_name':topic_name}
    group="year, month, day, hour"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_all_tag_views(sql_obj,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, Tags.tag_name"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Tags ON Post.article_ID=Tags.article_ID"
    group='Tags.tag_name'
    return sql_obj.select(find,table,groupby=group)

def stat_tag_views(sql_obj,tag_name,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Tags ON Post.article_ID=Tags.article_ID"
    conditions={'Tags.tag_name':tag_name}
    return sql_obj.select(find,table,conditions=conditions)

def stat_views_tag_time(sql_obj,tag_name,unique=False):
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Tags ON Post.article_ID=Tags.article_ID"
    conditions={'Tags.tag_name':tag_name}
    group="year, month, day, hour"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_author_views(sql_obj,author_name,unique=False):
    author = author_name.split(' ')
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID"
    conditions={'Users.first_name':author[0],'Users.last_name':author[1]}
    return sql_obj.select(find,table,conditions=conditions)

def stat_contributor_views(sql_obj,author_name,unique=False):
    author = author_name.split(' ')
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Contributes ON Contributes.article_ID=Post.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID"
    conditions={'Users.first_name':author[0],'Users.last_name':author[1]}
    return sql_obj.select(find,table,conditions=conditions)

def stat_author_views_time(sql_obj,author_name,unique=False):
    author = author_name.split(' ')
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID"
    conditions={'Users.first_name':author[0],'Users.last_name':author[1]}
    group="year, month, day, hour"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_contributor_views_time(sql_obj,author_name,unique=False):
    author = author_name.split(' ')
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Contributes ON Contributes.article_ID=Post.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID"
    conditions={'Users.first_name':author[0],'Users.last_name':author[1]}
    group="year, month, day, hour"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_author_topic_views(sql_obj,author_name,unique=False):
    author = author_name.split(' ')
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, Topic_Post.topic_name"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID"
    conditions={'Users.first_name':author[0],'Users.last_name':author[1]}
    group="topic_name"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_contributor_topic_views(sql_obj,author_name,unique=False):
    author = author_name.split(' ')
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, Topic_Post.topic_name"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Contributes ON Contributes.article_ID=Post.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID"
    conditions={'Users.first_name':author[0],'Users.last_name':author[1]}
    group="topic_name"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_author_topic_views_time(sql_obj,author_name,topic_name,unique=False):
    author = author_name.split(' ')
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Writes ON Writes.article_ID=Post.article_ID INNER JOIN Users ON Writes.author_ID=Users.ID INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID"
    conditions={'Users.first_name':author[0],'Users.last_name':author[1],'Topic_Post.topic_name':topic_name}
    group="year, month, day, hour"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_contributor_topic_views_time(sql_obj,author_name,topic_name,unique=False):
    author = author_name.split(' ')
    unique = 'DISTINCT' if unique else ''
    find=f"COUNT({unique} IP_address) AS viewers, visit, YEAR(visit) as year ,MONTH(visit) as month, DAY(visit) as day, HOUR(visit) as hour"
    table="Stats INNER JOIN Post on Stats.article_ID=Post.article_ID INNER JOIN Contributes ON Contributes.article_ID=Post.article_ID INNER JOIN Users ON Contributes.contributor=Users.ID INNER JOIN Topic_Post on Post.article_ID=Topic_Post.article_ID"
    conditions={'Users.first_name':author[0],'Users.last_name':author[1],'Topic_Post.topic_name':topic_name}
    group="year, month, day, hour"
    return sql_obj.select(find,table,conditions=conditions,groupby=group)

def stat_site_subs(sql_obj):
    find='COUNT(sub_email) AS count_subs'
    table="Subscribes"
    return sql_obj.select(find,table)

def stat_all_topic_subs(sql_obj):
    find='COUNT(Subscribes.sub_email) AS count_subs, Subscribes.topic_name'
    table="Subscribes INNER JOIN Topics ON Subscribes.topic_name=Topics.topic_name"
    group="Subscribes.topic_name"
    return sql_obj.select(find,table,groupby=group)

def stat_topic_subs(sql_obj,topic_name):
    find='COUNT(Subscribes.sub_email) AS count_subs'
    table="Subscribes"
    conditions={"topic_name":topic_name}
    return sql_obj.select(find,table,conditions=conditions)

def stat_membership_subs(sql_obj):
    find='COUNT(sub_email) AS count_subs, membership'
    table="Subscribes"
    group="membership"
    return sql_obj.select(find,table,groupby=group)

def stat_all_author_subs(sql_obj):
    find='COUNT(author) AS count_subs, author'
    table="(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID GROUP BY author, topic_name) AS U INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name"
    group="author"
    return sql_obj.select(find,table,groupby=group)

def stat_author_subs(sql_obj, author_name):
    find='COUNT(author) AS count_subs, author'
    table="(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID GROUP BY author, topic_name) AS U INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name"
    conditions={"author":author_name}
    return sql_obj.select(find,table,conditions=conditions)

def stat_all_contributor_subs(sql_obj):
    find='COUNT(author) AS count_subs, author'
    table="(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author FROM Users INNER JOIN Contributes ON Users.ID=Contributes.contributor INNER JOIN Topic_Post ON Contributes.article_ID=Topic_Post.article_ID GROUP BY author, topic_name) AS U INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name"
    group="author"
    return sql_obj.select(find,table,groupby=group)

def stat_all_contributor_subs(sql_obj,contrib_name):
    find='COUNT(author) AS count_subs, author'
    table="(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author FROM Users INNER JOIN Contributes ON Users.ID=Contributes.contributor INNER JOIN Topic_Post ON Contributes.article_ID=Topic_Post.article_ID GROUP BY author, topic_name) AS U INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name"
    conditions={"author":contrib_name}
    return sql_obj.select(find,table,conditions=conditions)

def stat_site_revenue(sql_obj):
    find='SUM(trans_amount)'
    table='Revenue'
    return sql_obj.select(find,table)

def stat_all_topics_revenue(sql_obj):
    find='SUM(trans_amount), Topics.topic_name'
    table="Revenue INNER JOIN Subscribes ON Revenue.sub_email=Subscribes.sub_email INNER JOIN Topics ON Subscribes.topic_name=Topics.topic_name"
    group="Topics.topic_name"
    return sql_obj.select(find,table,groupby=group)

def stat_topic_revenue(sql_obj,topic_name):
    find='SUM(trans_amount), Topics.topic_name'
    table="Revenue INNER JOIN Subscribes ON Revenue.sub_email=Subscribes.sub_email INNER JOIN Topics ON Subscribes.topic_name=Topics.topic_name"
    conditions={"Topics.topic_name":topic_name}
    return sql_obj.select(find,table,conditions=conditions)

def stat_all_author_revenue(sql_obj):
    find='SUM(author) AS count_subs, author'
    table="(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID GROUP BY author, topic_name) AS U INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name INNER JOIN Revenue ON Subscribes.sub_email=Revenue.sub_email"
    group="author"
    return sql_obj.select(find,table,groupby=group)

def stat_author_revenue(sql_obj, author_name):
    find='SUM(author) AS count_subs, author'
    table="(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author FROM Users INNER JOIN Writes ON Users.ID=Writes.author_ID INNER JOIN Topic_Post ON Writes.article_ID=Topic_Post.article_ID GROUP BY author, topic_name) AS U INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name INNER JOIN Revenue ON Subscribes.sub_email=Revenue.sub_email"
    conditions={"author":author_name}
    return sql_obj.select(find,table,conditions=conditions)

def stat_all_contributor_revenue(sql_obj):
    find='SUM(author) AS count_subs, author'
    table="(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author FROM Users INNER JOIN Contributes ON Users.ID=Contributes.contributor INNER JOIN Topic_Post ON Contributes.article_ID=Topic_Post.article_ID GROUP BY author, topic_name) AS U INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name INNER JOIN Revenue ON Subscribes.sub_email=Revenue.sub_email"
    group="author"
    return sql_obj.select(find,table,groupby=group)

def stat_all_contributor_revenue(sql_obj,contrib_name):
    find='SUM(author) AS count_subs, author'
    table="(SELECT topic_name, CONCAT(Users.first_name,' ',Users.last_name) as author FROM Users INNER JOIN Contributes ON Users.ID=Contributes.contributor INNER JOIN Topic_Post ON Contributes.article_ID=Topic_Post.article_ID GROUP BY author, topic_name) AS U INNER JOIN Subscribes ON U.topic_name=Subscribes.topic_name INNER JOIN Revenue ON Subscribes.sub_email=Revenue.sub_email"
    conditions={"author":contrib_name}
    return sql_obj.select(find,table,conditions=conditions)


if __name__=="__main__":
    Q = custom_SQL()

    s2 = stat_site_views(Q)

    Q.close()
    print(s2)