"""
The flask application package.
"""

# Code Added for Azure AppInsight
from applicationinsights.flask.ext import AppInsights
# End of code Azure AppInsight

from flask import Flask
app = Flask(__name__)

# Code Added for Azure AppInsight
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'MY_INSTRUMENTATION_KEY'
#'<YOUR INSTRUMENTATION KEY GOES HERE>'

# log requests, traces and exceptions to the Application Insights service
appinsights = AppInsights(app)
# End of code Azure AppInsight

import python_webapp_flask.views

import os
import logging
# import log information on stdout
from logging import StreamHandler
# keep stdout/stderr logging using StreamHandler
streamHandler = StreamHandler()
app.logger.addHandler(streamHandler)
# define log level to DEBUG
app.logger.setLevel(logging.DEBUG)

# force flushing application insights handler after each request
@app.after_request
def after_request(response):
    appinsights.flush()
    return response