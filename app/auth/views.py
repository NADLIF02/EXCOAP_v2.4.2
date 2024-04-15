from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validation logic here
        session['logged_in'] = True
        return redirect(url_for('calendar.display'))
    return render_template('auth/login.html')
