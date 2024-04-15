from flask import Blueprint, render_template, session, redirect, url_for

calendar = Blueprint('calendar', __name__, url_prefix='/calendar')

@calendar.route('/')
def display():
    if not session.get('logged_in'):
        return redirect(url_for('auth.login'))
    return render_template('event_calendar/calendar.html')
