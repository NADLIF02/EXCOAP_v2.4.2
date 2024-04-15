from flask import Blueprint
from .views import calendar


calendar = Blueprint('calendar', __name__)

from . import views
