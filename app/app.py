from flask import Flask, request, render_template, redirect, url_for, flash
from flask_bcrypt import Bcrypt
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_ici'
bcrypt = Bcrypt(app)

def get_db_connection():
    try:
        conn = psycopg2.connect("dbname=nom_de_votre_base_de_donnees user=utilisateur password=mot_de_passe")
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database: ", str(e))
        return None

@app.route('/')
def index():
    # Notez le chemin mis à jour ici pour le template
    return render_template('auth/login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = get_db_connection()
    if conn is None:
        flash('Database connection error.', 'error')
        return redirect(url_for('index'))
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cur.execute("SELECT mot_de_passe FROM utilisateurs WHERE nom_utilisateur = %s", (username,))
        user_record = cur.fetchone()
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        flash('An error occurred while fetching user data.', 'error')
        print("Query failed: ", str(e))
        return redirect(url_for('index'))

    if user_record and bcrypt.check_password_hash(user_record['mot_de_passe'], password):
        return redirect(url_for('dashboard'))
    else:
        flash('Nom d\'utilisateur ou mot de passe incorrect.', 'error')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return 'Bienvenue dans votre tableau de bord!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
