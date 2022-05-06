from flask import Flask, request
from common import common_routes
from facebook import facebook_routes
from google import google_routes

app = Flask(__name__)
common_routes(app)
google_routes(app)
facebook_routes(app)

