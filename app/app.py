from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from event_calendar.forms import EventForm  # Make sure this path is correct and EventForm is defined in forms.py

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure this key is kept secret in production environments

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))
    form = EventForm()  # Proper usage of forms for rendering
    return render_template('event_calendar/calendar.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add verification logic here to check username and password against a database or other storage
        session['logged_in'] = True
        return redirect(url_for('home'))
    return render_template('auth/login.html')

@app.route('/get-events', methods=['GET'])
def get_events():
    # This should ideally fetch from a database
    events = [
        {'title': 'Alice - Leave', 'start': '2024-04-15', 'end': '2024-04-18'},
        {'title': 'Bob - Leave', 'start': '2024-04-20', 'end': '2024-04-22'}
    ]
    return jsonify(events)

@app.route('/get-user-leaves', methods=['GET'])
def get_user_leaves():
    # This should ideally fetch from a database
    user_leaves = [
        {'user': 'Alice', 'start': '2024-04-15', 'end': '2024-04-18'},
        {'user': 'Bob', 'start': '2024-04-20', 'end': '2024-04-22'}
    ]
    return jsonify(user_leaves)

@app.route('/submit-leave', methods=['POST'])
def submit_leave():
    data = request.form
    start_date = data['start']
    end_date = data['end']
    description = data['description']
    # Insert logic to save the leave request to the database
    # For now, simulate a response with the submitted data
    return jsonify({
        'title': description,
        'start': start_date,
        'end': end_date
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
