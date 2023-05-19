"""
The flask application package.
"""

#from markupsafe import Markup

from flask import Flask
app = Flask(__name__)

import python_webapp_flask.views
