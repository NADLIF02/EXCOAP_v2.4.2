from flask import Blueprint
from .views import auth

auth = Blueprint('auth', __name__)

from . import views
