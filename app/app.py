from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_ici'
bcrypt = Bcrypt(app)

def get_db_connection():
    try:
        return psycopg2.connect("dbname=nom_de_votre_base_de_donnees user=utilisateur password=mot_de_passe")
    except psycopg2.Error as e:
        print("Unable to connect to the database: ", str(e))
        return None

@app.route('/')
def index():
    return render_template('auth/login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = get_db_connection()
    if not conn:
        flash('Database connection error.', 'error')
        return redirect(url_for('index'))
    
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT mot_de_passe FROM utilisateurs WHERE nom_utilisateur = %s", (username,))
            user_record = cur.fetchone()
    except psycopg2.Error as e:
        flash('An error occurred while fetching user data.', 'error')
        print("Query failed: ", str(e))
    finally:
        conn.close()

    if user_record and bcrypt.check_password_hash(user_record['mot_de_passe'], password):
        session['user_id'] = username  # Example of setting session
        return redirect(url_for('dashboard'))
    else:
        flash('Nom d\'utilisateur ou mot de passe incorrect.', 'error')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('index'))
    return 'Bienvenue dans votre tableau de bord, {}'.format(session['user_id'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
