from flask import Blueprint, render_template, request, redirect, url_for, session

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('.login'))
    else:
        return render_template('event_calendar/calendar.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Ajouter la logique de vérification ici
        session['logged_in'] = True
        return redirect(url_for('.home'))
    return render_template('auth/login.html')
