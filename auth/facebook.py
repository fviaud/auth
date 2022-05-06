from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
import os

def facebook_routes(app):
    app.secret_key = '!secret'
    app.config.from_object('config')
    oauth = OAuth(app)
    CONF_URL = 'https://www.facebook.com/.well-known/openid-configuration/'
    oauth.register(
        name='facebook',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        server_metadata_url=CONF_URL,
        client_kwargs={'scope': 'email'},
    )

    @app.route('/api/auth/login/facebook')
    def login_facebook():
        redirect_uri = url_for('auth_facebook', _external=True)
        return oauth.facebook.authorize_redirect(redirect_uri)

    @app.route('/api/auth/callback/facebook')
    def auth_facebook():
        token = oauth.facebook.authorize_access_token()
        resp = oauth.facebook.get('https://graph.facebook.com/me?fields=id,name,email,picture{url}')
        user = resp.json()
        if user:
            session['user'] = user
        return redirect('/')

