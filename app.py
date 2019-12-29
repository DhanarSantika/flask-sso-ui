from flask import Flask, redirect
from flask_sso_ui.decorators import login_sso_ui, logout_sso_ui
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
@login_sso_ui(force_login=True)
def login(sso_profile):
    return json.dumps(sso_profile)

@app.route('/logout')
@logout_sso_ui
def logout():
    pass