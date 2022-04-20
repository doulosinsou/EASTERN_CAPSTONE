# from types import NoneType
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
    # print('/ index?')
    # if page in ['topics','topic','viewas']:
    #     print("Made it past page in [***]")
    #     return redirect(page)
    
    Q = custom_SQL()
    page = customSQL.grab_article(Q,page)
    Q.close()
    post = {
        'title': page['title'][0],
        'content': page['content'][0],
        'username': session['email']
    }

    user = True if session['role'] in ['admin','author','contributor'] else False

    template=page['page_type'][0]+'.html'

    return render_template(
        template, 
        post=post,
        user=user,
        role=session['role'],
        )

@app.route('/topic/')
@app.route('/Topic')
@app.route('/topic/<thisTopic>')
@app.route("/topic/<thisTopic>/<title>")
def sortTopic(thisTopic=None,title=None):
    if thisTopic and title:
        return prepTopic(thisTopic,title)
    elif thisTopic:
        return aboutTop(thisTopic)
    else:
        return redirect('/topics/')

def aboutTop(thisTopic):
    Q = custom_SQL()
    topic_list = customSQL.grab_articles_in_topic(Q,thisTopic,order="ASC")
    Q.close()
    return render_template('topic.html', 
        topic= {
            "post_title":topic_list['title'],
            "topic_name":thisTopic,
            "topic_status":topic_list['topic_status'][0],
            "topic_description":topic_list['topic_description'][0]
        },
        role=session['role'],
        )

def prepTopic(thisTopic="Project",title="Project Goals"):
    #Deliver page post
    Q = custom_SQL()
    article = customSQL.grab_article(Q,title)
    tops = customSQL.grab_topics_in_article(Q,article['article_ID'][0])
    previous = customSQL.grab_kin_article(Q,article['title'][0],thisTopic,"-1")
    after = customSQL.grab_kin_article(Q,article['title'][0],thisTopic,"1")
    toplist = customSQL.grab_articles_in_topic(Q,thisTopic,order="ASC")
    tags = customSQL.grab_tags_in_article(Q,article['article_ID'][0])

    Q.close()

    i=0
    post = {
        'title':article['title'][i],
        'author':article['author'][i],
        'date':article['post_date'][i],
        'subtitle':article['subtitle'][i],
        'topics':', '.join(tops['topic_name']),
        'tags':', '.join(tags['tag_name']),
        'content': article['content'][i],
        'previous':previous['title'][0],
        'next':after['title'][0]
        }
    topic_ = {
        'name':thisTopic,
        'list':toplist['title'],
    }

    return render_template('post.html', 
        post=post,
        topic=topic_,
        role=session['role'],
        )


@app.route("/Topics/")
@app.route("/topics/")
def topics():
    Q = custom_SQL()
    topic_list= customSQL.grab_all_topics(Q)
    Q.close()

    return render_template('topics.html', 
        topic_list=topic_list,
        )


@app.route('/feed/')
def feed():
    Q = custom_SQL()
    email = session['email']

    if email == None:
        availableTopics = customSQL.grab_public_topics(Q)
        feed = customSQL.grab_article_feed("basicSubscriber@subs.org")
    else:   
        availableTopics = customSQL.grab_subscribed_topics(Q,email)
        feed = customSQL.grab_article_feed(Q,email)
    Q.close()

    return render_template('feed.html', 
        availableTopics=availableTopics,
        email=email,
        role=session['role'],
        Feed=feed,

        )

@app.route('/tags/')
@app.route('/tag/')
@app.route('/Tags/')
def aboutTag():
    Q = custom_SQL()
    tag_list= customSQL.grab_all_tags(Q)
    Q.close()

    return render_template('tags.html', 
        tag_list=tag_list,
        )


@app.route('/tag/<tagname>')
def prepTag(tagname='public'):
    Q = custom_SQL()
    article_list= customSQL.grab_articles_in_tag(Q, tagname)
    Q.close()

    return render_template('tag_page.html', 
        tag=tagname,
        article_list=article_list,
        )

@app.route('/about/')
@app.route('/authors/')
@app.route('/author/')
def allAuthors():
    Q = custom_SQL()
    authors= customSQL.grab_authors(Q)
    contributors=customSQL.grab_contributors(Q)
    Q.close()

    return render_template('about.html', 
        authors=authors,
        contributors=contributors,
        )

@app.route('/author/<author>')
def aboutAuthor(author=None):
    Q = custom_SQL()
    if " " in author:
        author = author.split(' ')
    elif "-" in author:
        author = author.split('-')
    profile= customSQL.grab_about_author(Q,author[0],author[1])
    articles = customSQL.grab_author_articles(Q, profile['ID'][0])
    contribs = customSQL.grab_contributor_articles(Q, profile['ID'][0])
    Q.close()


    def sort_topic(query):
        by_topic = {}
        for (topic, title) in zip(query['topic_name'],query['title']):
            if topic not in by_topic.keys():
                by_topic[topic] = []
            by_topic[topic].append(title)
        return by_topic

    auth_by_topic = sort_topic(articles)
    contrib_by_topic = sort_topic(contribs)

    return render_template('author.html', 
        author={
            "name":profile['first_name'][0]+' '+profile['last_name'][0],
            "role":profile['user_role'][0],
            "date":profile['date'][0],
            "days_employed":profile['days_employed'][0],
            "email":profile['email'][0],
            "biography":profile['biography'][0],
            "avatar_link":profile['avatar_link'][0]
        },
        articles=auth_by_topic if len(articles) else False,
        contribs=contrib_by_topic if len(contribs) else False
        )


@app.route('/viewas/', methods=['POST'])
def viewas():
    viewer=request.form['logged-in']
    Q = custom_SQL()
    role = customSQL.grab_role(Q,viewer)
    Q.close()
    if role['role'] == []:
        session['role'] = "Public"
    else:
        session['role'] = role['role'][0]
    session['email'] = viewer
    

    return redirect('/feed/')

    # viewas=request.form['logged-in']
    # resp = make_response(redirect(request.referrer))
    # resp.set_cookie('email',viewas)

    # Q = custom_SQL()
    # role = customSQL.grab_role(Q,viewas)
    # resp.set_cookie('role',role['role'][0])

    # return resp
