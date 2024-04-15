from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .forms import LoginForm  # Import correct du formulaire

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Création d'une instance du formulaire
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Supposons que USERS soit défini quelque part pour valider les identifiants
        if username in USERS and USERS[username] == password:
            session['logged_in'] = True
            flash('Vous êtes maintenant connecté!', 'success')
            return redirect(url_for('event_calendar.display'))
        else:
            flash('Identifiant ou mot de passe incorrect!', 'error')
    return render_template('auth/login.html', form=form)
