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



if __name__=="__main__":
    Q = custom_SQL()

    s2 = stat_site_views(Q)

    Q.close()
    print(s2)