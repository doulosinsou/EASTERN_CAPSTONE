from flask import Flask, render_template, redirect, url_for, request, make_response, session
from datetime import datetime

import customSQL
from customSQL import custom_SQL




app = Flask(__name__)

#default dummy key for now
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.before_request
def check_user():
    if 'email' in session:
        email = session['email']
        print(email)
    if 'role' in session: 
        role = session['role']
        print(role)
    

@app.route('/')
def index():
    pass
    # Q = custom_SQL()
    # homepage = customSQL.grab_article(Q)

@app.route("/Topic/<thisTopic>/<title>")
@app.route("/Topics/")
def sortTopic(thisTopic=None,title=None):
    if thisTopic and title:
        return category(thisTopic,title)
    elif thisTopic:
        return aboutCat(thisTopic)
    
    Q = custom_SQL()

    email = session['email']
    if email == None:
        availableTopics = customSQL.grab_public_topics(Q)
    else:   
        availableTopics = customSQL.grab_subscribed_topics(Q,email)

    print(availableTopics['topic_name'])

    return category()


def aboutCat(thisTopic):
    pass

def category(thisTopic="Project",title="Project Goals"):


    #Deliver page post
    Q = custom_SQL()
    article = customSQL.grab_article(Q,title)
    cats = customSQL.grab_topics_in_article(Q,article['article_ID'][0])
    previous = customSQL.grab_kin_article(Q,article['title'][0],thisTopic,"-1")
    after = customSQL.grab_kin_article(Q,article['title'][0],thisTopic,"1")
    catlist = customSQL.grab_articles_in_topic(Q,thisTopic)
    tags = customSQL.grab_tags_in_article(Q,article['article_ID'][0])

    Q.close()

    i=0
    post = {
        'title':article['title'][i],
        'author':article['author'][i],
        'date':article['post_date'][i],
        'subtitle':article['subtitle'][i],
        'topics':', '.join(cats['topic_name']),
        'tags':', '.join(tags['tag_name']),
        'content': article['content'][i],
        'previous':previous['title'][0],
        'next':after['title'][0]
        }
    topic_ = {
        'name':thisTopic,
        'list':catlist['title'],
    }

    return render_template('topic.html', 
        post=post,
        topic=topic_,
        admin=True
        )

@app.route('/viewas/', methods=['POST'])
def viewas():
    viewer=request.form['logged-in']
    Q = custom_SQL()
    role = customSQL.grab_role(Q,viewer)
    session['email'] = viewer
    session['role'] = role['role'][0]

    return make_response(redirect(request.referrer))

    # viewas=request.form['logged-in']
    # resp = make_response(redirect(request.referrer))
    # resp.set_cookie('email',viewas)

    # Q = custom_SQL()
    # role = customSQL.grab_role(Q,viewas)
    # resp.set_cookie('role',role['role'][0])

    # return resp
