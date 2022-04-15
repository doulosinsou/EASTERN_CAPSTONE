from flask import Flask, render_template
from datetime import datetime

import customSQL
from customSQL import custom_SQL




app = Flask(__name__)

@app.route('/')
@app.route("/<category>")
def home(category="home"):

    #Deliver page post
    Q = custom_SQL()
    find='*'
    table='Post'
    conditions={"theme":"Dark-wide","page_type":"blog"}
    findCat = Q.select(find,table,conditions,where=True)



    # print(findCat)
    Q.close()

    i = 1

    post = {
        'title':findCat['title'][i],
        'author':"?",
        'date':findCat['post_date'][i],
        'subtitle':findCat['subtitle'][i],
        'categories':'?',
        'tags':'?',
        'content': findCat['content'][i],
        'previous':'',
        'next':'Second Post'
        }
    category = {
        'name':"demo",
        'list':['Second Post','Third Post','Fourth Post'],
    }

    return render_template('category.html', 
    post=post,
    category=category,
    admin=True
    )

