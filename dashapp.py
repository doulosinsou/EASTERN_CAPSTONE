from flask import Blueprint, render_template, session, request, redirect,jsonify, send_file

import dashboard
# from dashboard import *
import customSQL
from customSQL import custom_SQL

dashapp = Blueprint('dashapp',__name__,template_folder='templates')

@dashapp.route('/dashboard/')
def dashboard_():
    if session['role'] not in ['admin']:
        return redirect('/home')
    
    user_stats = {}
    if session['role'] == 'admin':
        pass
    if session['role'] == 'author':
        pass
    elif session['role'] == 'contributor':
        pass


    return render_template('dashboard.html',
        role=session['role']
    )


@dashapp.route('/stats', methods=['POST'])
def s():
    req = request.json


@dashapp.route('/stats/authors/', methods=['POST'])
def statsauthors():
    req = request.json
    print(req)
    Q = custom_SQL()
    to_return = []
    auth_stats = dashboard.stat_author_stats(Q)
    if req['type'] == 'views':
        func = dashboard.stat_author_views_time 
    else:
        func = dashboard.stat_author_subs_time

    for i in range(len(auth_stats['author'])):
        name = auth_stats['author'][i]
        to_return.append({
            "author":auth_stats['author'][i],
            "avatar":auth_stats['avatar_link'][i],
            "posts":auth_stats['post'][i],
            "revenue":auth_stats['revenue'][i],
            "views":func(Q,name,req['year'],req['month'],req['unique'])
            })
    # print(to_return)
    Q.close()
    return jsonify(to_return)
    

@dashapp.route('/stats/views-time/', methods=['POST'])
def viewstime():
    req = request.json
    Q = custom_SQL()
    if req['type'] == 'views':
        views = dashboard.stat_views_site_time(Q,req['year'],req['month'],req['unique'])
        return jsonify(views)
    elif req['type'] == 'subs':
        subs = dashboard.stat_subs_site_time(Q,req['year'],req['month'],req['unique'])
        return jsonify(subs)

@dashapp.route('/stats/views-type/', methods=['POST'])
def viewstype():
    req = request.json
    Q = custom_SQL()
    if req['category'] == 'tag':
        if req['type'] == 'views':
            views = dashboard.stat_views_tag_time(Q,req['year'],req['month'])
            return jsonify(views)
        if req['type'] == 'subs':
            views = dashboard.stat_subs_tag_time(Q,req['year'],req['month'])
            return jsonify(views)
    if req['category'] == 'topic':
        if req['type'] == 'views':
            views = dashboard.stat_all_topic_views_time(Q,req['year'],req['month'])
            return jsonify(views)
        if req['type'] == 'subs':
            views = dashboard.stat_all_topic_subs_time(Q,req['year'],req['month'])
            
            return jsonify(views)

@dashapp.route('/stats/kpi/', methods=['POST'])
def stats():
    Q = custom_SQL()
    req = request.json
    if req['request'] == "KPI_av":
        kpi = dashboard.kpi_site_view_av_day_month(Q,req['year'],req['month'])
        if kpi[0][0]<10:
            fillColor = 'orange'
        elif kpi[0][0]<25:
            fillColor = 'yellow'
        else:
            fillColor = 'green'
        
        return jsonify({"fillColor":fillColor,"kpi":kpi[0]})
    elif req['request'] == "KPI_goal":
        kpi = dashboard.kpi_site_month_goals(Q,req['year'],req['month'])
        if kpi[0][0]<65:
            fillColor = 'red'
        elif kpi[0][0]<90:
            fillColor = 'orange'
        else:
            fillColor = 'green'
        
        return jsonify({"fillColor":fillColor,"kpi":kpi[0]})
    

@dashapp.route('/img/<filename>', methods=['GET'])
def showimg(filename):
    return send_file('static/img/'+filename,mimetype='image/png')