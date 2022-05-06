from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
import os

def common_routes(app):
    @app.route('/')
    def homepage():
        user = session.get('user')
        return render_template('home.html', user=user)

    @app.route('/api/auth/logout')
    def logout():
        session.pop('user', None)
        return redirect('/')