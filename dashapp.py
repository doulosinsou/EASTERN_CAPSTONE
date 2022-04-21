from flask import Blueprint, render_template, session, request, redirect

dashapp = Blueprint('dashapp',__name__,template_folder='templates')

@dashapp.route('/dashboard/')
def dashboard():
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
def stats():
    req = request.form


