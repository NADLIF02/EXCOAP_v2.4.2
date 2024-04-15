from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .forms import LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in USERS and check_password_hash(USERS[username], password):  # Utilisation de hachage
            session['logged_in'] = True
            flash('Vous êtes maintenant connecté!', 'success')
            return redirect(url_for('calendar.display'))  # Correction ici
        else:
            flash('Identifiant ou mot de passe incorrect!', 'error')
    return render_template('auth/login.html', form=form)
