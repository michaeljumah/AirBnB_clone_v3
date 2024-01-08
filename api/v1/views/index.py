#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request

@app_views.route('/', methods=['GET'], strict_slashes=False)
def index():
    return jsonify({'message': 'Hello, this is the API version 1!'})
@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({'status': 'OK'})
