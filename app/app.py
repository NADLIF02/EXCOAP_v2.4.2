from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))
    form = EventForm()  # Assuming EventForm is properly imported
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

@app.route('/get-events', methods=['GET'])
def get_events():
    # Example static data, replace with database query results
    events = [
        {'title': 'Alice - Leave', 'start': '2024-04-15', 'end': '2024-04-18'},
        {'title': 'Bob - Leave', 'start': '2024-04-20', 'end': '2024-04-22'}
    ]
    return jsonify(events)

@app.route('/get-user-leaves', methods=['GET'])
def get_user_leaves():
    # Example static data, replace with database query results
    user_leaves = [
        {'user': 'Alice', 'start': '2024-04-15', 'end': '2024-04-18'},
        {'user': 'Bob', 'start': '2024-04-20', 'end': '2024-04-22'}
    ]
    return jsonify(user_leaves)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
