from flask import Flask, render_template, request, redirect, url_for, session
from event_calendar.forms import EventForm  # Adjusted import

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))
    form = EventForm()  # Create an instance of the form
    return render_template('event_calendar/calendar.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Verification logic here
        session['logged_in'] = True
        return redirect(url_for('home'))
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
