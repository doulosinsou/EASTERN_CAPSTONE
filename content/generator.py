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

from xml.dom import minidom

def get_str(parent,child):
    return parent.getElementsByTagName(child)[0].childNodes[0].data

def get_list(parent,child):
    group = []
    taglist = parent.getElementsByTagName(child)
    for tag in taglist:
        for node in walk(tag.childNodes):
            group.append((tag.tagName, node))
    return group

def walk(parent):
    for child in parent:
        # if hasattr(child,'data') and not child.nodeType == child.TEXT_NODE:
        #     yield (parent,child.data)
        if child.nodeType != child.TEXT_NODE:
            yield (parent,child.data)
        else:
            walk(child.childNodes)
        # if child.nodeType != child.TEXT_NODE:
        #     for node in child.childNodes:
        #         yield (child.tagName,node.data)



file = minidom.parse('posts.xml')
post = file.getElementsByTagName('post')

for p in post:
    title = get_str(p,'title')
    author = get_list(p,'contributors')
    
    print(title, author)