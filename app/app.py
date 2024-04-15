from flask import Flask, request, render_template, redirect, url_for, flash
from flask_bcrypt import Bcrypt
import psycopg2

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_ici'
bcrypt = Bcrypt(app)

def get_db_connection():
    conn = psycopg2.connect("dbname=nom_de_votre_base_de_donnees user=utilisateur password=mot_de_passe")
    return conn

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT mot_de_passe FROM utilisateurs WHERE nom_utilisateur = %s", (username,))
    user_record = cur.fetchone()
    cur.close()
    conn.close()

    if user_record and bcrypt.check_password_hash(user_record[0], password):
        return redirect(url_for('dashboard'))
    else:
        flash('Nom d\'utilisateur ou mot de passe incorrect.', 'error')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return 'Bienvenue dans votre tableau de bord!'

if __name__ == '__main__':
    app.run(debug=True)
