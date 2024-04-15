from flask import Blueprint, render_template, request, redirect, url_for, session, flash

main = Blueprint('main', __name__)

# Route racine redirigeant selon l'état de connexion
@main.route('/')
def home():
    # Vérifie si l'utilisateur est déjà connecté
    if not session.get('logged_in'):
        return redirect(url_for('.login'))
    else:
        return redirect(url_for('.calendar'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Ajouter la logique de vérification ici (par exemple vérification contre une base de données)
        if username == 'admin' and password == 'secret':  # Cette partie doit être sécurisée et dynamique
            session['logged_in'] = True
            session['username'] = username  # Stocker le nom d'utilisateur dans la session
            return redirect(url_for('.home'))
        else:
            flash('Identifiant ou mot de passe incorrect.', 'error')

    # S'il n'est pas connecté ou si les identifiants sont incorrects
    return render_template('auth/login.html')

@main.route('/calendar')
def calendar():
    if not session.get('logged_in'):
        # Redirection vers la page de login si l'utilisateur n'est pas connecté
        return redirect(url_for('.login'))
    return render_template('event_calendar/calendar.html')

@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('.login'))
