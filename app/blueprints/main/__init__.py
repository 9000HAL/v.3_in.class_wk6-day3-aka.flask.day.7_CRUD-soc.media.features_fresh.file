from flask import Blueprint

main = Blueprint('main', __name__)

#from app.blueprints.main import routes #this is the only line that is different from the original---extra per GHCP

from . import routes


# Path: app/blueprints/main/routes.py