"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os, requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('chat.html')
@app.route('/login')
def login():
    
    return render_template('login.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/chat/<path:star>', methods=['GET'])
def send_text(star):
    return render_template("pchat.html", messages={'url':star})
    #return urllib.unquote(star).decode('utf8') 
    
@app.route('/anonchat/<path:star>', methods=['GET'])
def send_chatview(star):
    return render_template("vchat.html", messages={'url':star})
    #return urllib.unquote(star).decode('utf8') 
@app.route('/analytics/<path:star>', methods=['GET'])
def sentiment_view(star):
    return render_template("analytics.html", messages={'url':star})

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
