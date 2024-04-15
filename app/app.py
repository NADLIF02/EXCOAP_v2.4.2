from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from event_calendar.forms import EventForm  # Assurez-vous que ce chemin est correct

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète_très_sécurisée'  # Utilisez une clé secrète forte dans les environnements de production

# Route principale après connexion
@app.route('/')
def home():
    if not session.get('logged_in'):
        flash("Veuillez vous connecter pour accéder au calendrier.", "info")
        return redirect(url_for('login'))
    form = EventForm()
    return render_template('event_calendar/calendar.html', form=form)

# Route de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Ajoutez ici une logique de vérification contre une base de données
        user = find_user_by_username(username)
        if user and check_password_hash(user.password_hash, password):
            session['logged_in'] = True
            flash("Connexion réussie.", "success")
            return redirect(url_for('home'))
        else:
            flash("Identifiant ou mot de passe incorrect.", "error")
    return render_template('auth/login.html')

# Déconnexion
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("Vous avez été déconnecté.", "info")
    return redirect(url_for('login'))

# Gérer les routes pour les événements et les demandes de congé ici...

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
