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

def gather_posts(root, parser, code=False):
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

        if code:
            with open('content/'+'-'.join(post_dict['title'].split())+'.txt') as f:
                post_dict['content'] = str(f.read())
        else:
            post_dict['content'] = parser.tostring(findTag(post,'div')).decode("utf-8")
        
        postList.append(post_dict)
    
    return postList


def save_posts(posts,update=False):

    Q = custom_SQL() 
    for post in posts:
        if update:
            row_id = customSQL.grab_article(Q,post['title'])['article_ID']
            print(row_id, post['title'],post['content'][:30])
            Q.update('Post','content',post['content'],row_id[0])
            print()
        else:
            row_id = customSQL.put_article(Q, post['title'],post['subtitle'],post['theme'],post['content'],post['post_order'])
            print(row_id, post['title'])
            print()
            for topic in post['topics']:
                exists = Q.exists('topic_name','Topics',{'topic_name':topic['topic_name']})
                if not exists[0]:
                    Project_description = 'The topic reviews the whole process of building this website from scratch, including its underlying database and code'
                    proof = Q.insert('Topics',{'topic_name':topic['topic_name'],'topic_description':Project_description})
                    # Q.commit()
                customSQL.put_topic_post(Q,topic['topic_name'],row_id)

            for tag in post['tags']:
                customSQL.put_tag(Q,tag['tag_name'],row_id)

            author_id = customSQL.grab_author_id(Q,post['author'][2]['email'])
            customSQL.put_writes(Q,row_id,author_id["ID"][0])

            for contributor in post['contributors']:
                cont_id = customSQL.grab_author_id(Q,contributor['email'])
                customSQL.put_contributes(Q,row_id,cont_id['ID'][0])
        
    Q.commit()
    Q.close()




dumfile = ET.parse('content/dumposts.xml')
dumfeed = dumfile.getroot()
dumposts = gather_posts(dumfeed, ET)


codefile = ET.parse('content/codeposts.xml')
codefeed = codefile.getroot()
codeposts = gather_posts(codefeed, ET, code=True)

save_posts(dumposts)
save_posts(codeposts)

    


