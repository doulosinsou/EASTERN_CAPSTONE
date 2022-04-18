# import customSQL
# from customSQL import custom_SQL



# def put_post(sql_obj, post_data):
#     title = post_data[0]
#     subtitle = post_data[1]
#     theme = post_data[2]
#     page_type = "blog"
#     post_order = post_data[4]
#     content = post_data[5]
#     cover_img_link = post_data[6]

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

def gather_posts(root):
    postList = []

    for post in feed:
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
        post_dict['content'] = findTag(post,'content').text

        postList.append(post_dict)
    
    return postList

file = ET.parse('posts.xml')
feed = file.getroot()

posts = gather_posts(feed)

print(posts)