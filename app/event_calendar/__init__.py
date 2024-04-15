from flask import Blueprint
from .views import calendar

calendar = Blueprint('calendar', __name__, url_prefix='/calendar')

from . import views
