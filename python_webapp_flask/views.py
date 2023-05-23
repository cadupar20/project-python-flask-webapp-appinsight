"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from python_webapp_flask import app

@app.route('/')
@app.route('/home')
def home():
    app.logger.debug('This is a debug log message')
    app.logger.info('This is an information log message')
    app.logger.warn('This is a warning log message')
    app.logger.error('This is an error message')
    app.logger.critical('This is a critical message')
    
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# Code Added for Azure AppInsight (track_custom_event)
# Sending a custom event:
@app.route('/track_custom_event')
def track_custom_event():
    from applicationinsights import TelemetryClient
    tc = TelemetryClient(app.config['APPINSIGHTS_INSTRUMENTATIONKEY'])
    tc.track_event('ShoppingCartCheckout')
    tc.flush()
    return render_template('index.html')
# End of code Azure AppInsight

# Code Added for Azure AppInsight (send_metric)
@app.route('/send_metric')
def send_metric():
    from applicationinsights import TelemetryClient
    tc = TelemetryClient(app.config['APPINSIGHTS_INSTRUMENTATIONKEY'])
    import random
    tc.track_metric('queueSize',  random.randint(0,5000))
    tc.flush()
    return render_template('index.html')
# End of code Azure AppInsight

# Code Added for Azure AppInsight (HandledException)
# Logging an exception
@app.route('/handledException')
def handledException():
    import sys
    import string
    import random
    from applicationinsights import TelemetryClient
    tc = TelemetryClient(app.config['APPINSIGHTS_INSTRUMENTATIONKEY'])
    
    try:
        randomstring = ''.join([random.choice(string.ascii_letters) for n in xrange(8)])
        raise Exception("Exception {0}".format(randomstring))
    except:
       tc.track_exception()
   
    try:
       randomstring = ''.join([random.choice(string.ascii_letters) for n in xrange(8)])
       raise Exception("Exception {0}".format(randomstring))
    except:
       tc.track_exception(*sys.exc_info(), properties={ 'foo': 'bar' }, measurements={ 'x': 42 })
       tc.flush()
   
    return render_template('index.html')
# End of code Azure AppInsight