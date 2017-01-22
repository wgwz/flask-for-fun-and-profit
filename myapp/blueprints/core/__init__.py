from flask import Blueprint

blueprint = Blueprint('core', __name__)

from . import views