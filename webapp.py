from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route("/<name>")
def hello_world(name=None):
    post = {
        'title':'First Post',
        'author':'Lucas Moyer',
        'date':datetime.now(),
        'subtitle':'Testing Nested templates',
        'categories':'Demo, First',
        'tags':'testing',
        'content': "<p>Testing the first blog post</p><p>This is the first of many</p>",
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