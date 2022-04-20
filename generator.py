import customSQL
from customSQL import custom_SQL

import xml.etree.ElementTree as ET

def findTag(node,tagname):
    for n in node:
        if hasattr(n,'tag'):
            if n.tag == tagname:
                return n

def nested(node,tagname):
    group_list = []
    for item in findTag(node,tagname):
        nest_dict = dict()
        if 'type' in item.attrib.keys():
            for c in item:
                nest_dict[c.tag] = c.text 
        else:
            nest_dict[item.tag] = item.text
        group_list.append(nest_dict)
    return group_list

def gather_posts(root, parser):
    postList = []

    for post in root:
        post_dict = dict()

        post_dict['title'] = findTag(post,'title').text
        post_dict['subtitle'] = findTag(post,'subtitle').text
        post_dict['author'] = nested(post,'author')
        post_dict['contributors'] = nested(post,'contributors')
        post_dict['theme'] = findTag(post,'theme').text
        post_dict['topics'] = nested(post,'topics')
        post_dict['tags'] = nested(post,'tags')
        post_dict['post_order'] = int(findTag(post,'post_order').text)
        post_dict['cover_img_link'] = findTag(post,'cover_img_link').text
        post_dict['content'] = parser.tostring(findTag(post,'div'))

        
        postList.append(post_dict)
    
    return postList


file = ET.parse('content/posts.xml')
feed = file.getroot()
posts = gather_posts(feed, ET)

for post in posts[:1]:
    Q = custom_SQL() 

    row_id = customSQL.put_article(Q, post['title'],post['subtitle'],post['theme'],post['content'],post['post_order'])

    for topic in post['topics']:
        customSQL.put_topic_post(Q,topic['topic_name'],row_id)

    for tag in post['tags']:
        # if not Q.exists('tag_name','Tags',tag['tag_name'],{'article_ID':row_id}):
        customSQL.put_tag(Q,tag,row_id)

    author_id = customSQL.grab_author_id(Q,post['author']['email'])
    customSQL.put_writes(Q,row_id,author_id)

    for contributor in topic['contributors']:
        cont_id = customSQL.grab_author_id(Q,contributor['email'])
        customSQL.put_contributes(Q,row_id,cont_id)

    Q.close()
    
Q= custom_SQL
findinsert = customSQL.grab_article(Q,posts[0]['title'])
print(findinsert['title'][0])
