#!/usr/bin/python3
"""
flask route on the object app_views that returns a JSON status
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """
    create a route /status on the object app_views that returns a JSON
    """
    resp = {"status": "OK"}
    return jsonify(resp)
