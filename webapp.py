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
@app.route('/<page>')
def index(page='home'):
    if page in ['topics','topic','viewas']:
        return redirect(url_for(page))
    
    Q = custom_SQL()
    page = customSQL.grab_article(Q,page)

    post = {
        'title': page['title'][0],
        'content': page['content'][0],
        'username': session['email']
    }

    template=page['page_type'][0]+'.html'
    return render_template(template, post=post)


@app.route("/topic/<thisTopic>/<title>")
def sortTopic(thisTopic=None,title=None):
    print(thisTopic, title)
    if thisTopic and title:
        return category(thisTopic,title)
    elif thisTopic:
        return aboutCat(thisTopic)
    else:
        return redirect(url_for('/topics'))

    
    # Q = custom_SQL()

    # email = session['email']
    # if email == None:
    #     availableTopics = customSQL.grab_public_topics(Q)
    # else:   
    #     availableTopics = customSQL.grab_subscribed_topics(Q,email)

    # print('availableTopics')
    # print(availableTopics['topic_name'])

    # return category()

def aboutCat(thisTopic):
    return "About "+thisTopic

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


@app.route("/topics/")
def topics():
    Q = custom_SQL()
    email = session['email']

    if email == None:
        availableTopics = customSQL.grab_public_topics(Q)
        feed = customSQL.grab_article_feed("basicSubscriber@subs.org")
    else:   
        availableTopics = customSQL.grab_subscribed_topics(Q,email)
        feed = customSQL.grab_article_feed(Q,email)

    print('feed:')
    print(feed)
    print('availableTopics')
    print(availableTopics)

    return render_template('list.html', 
        availableTopics=availableTopics,
        email=email,
        role=session['role'],
        Feed=feed,
        )




@app.route('/viewas/', methods=['POST'])
def viewas():
    viewer=request.form['logged-in']
    Q = custom_SQL()
    role = customSQL.grab_role(Q,viewer)
    session['email'] = viewer
    session['role'] = role['role'][0]

    return make_response(redirect(url_for('/topics')))

    # viewas=request.form['logged-in']
    # resp = make_response(redirect(request.referrer))
    # resp.set_cookie('email',viewas)

    # Q = custom_SQL()
    # role = customSQL.grab_role(Q,viewas)
    # resp.set_cookie('role',role['role'][0])

    # return resp
