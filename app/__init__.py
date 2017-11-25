from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

bootstrap = Bootstrap()
moment = Moment()

app = Flask(__name__)

bootstrap.init_app(app)
moment.init_app(app)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

from app import views
