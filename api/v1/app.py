#!/usr/bin/python3
"""
Flask Api start
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template, url_for, Blueprint
import os

app = Flask(__name__)
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    """Run flask server
    (variable app)
    """
    app.run(host=host, port=port, threaded=True)
