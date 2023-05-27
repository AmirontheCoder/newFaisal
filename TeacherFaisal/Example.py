from flask import Flask, render_template, request, redirect, url_for, session, abort, flash, make_response
from PyDictionary import PyDictionary
from googletrans import Translator
import mysql.connector
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pathlib
import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
from google.auth.transport.requests import Request
import google.auth.transport.requests
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField

app = Flask(__name__, static_url_path='/static')
app.secret_key = "AmirKhoury"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scorePage")
def scorePage():
    return render_template("score.html")

def is_authenticated():
    return "google_id" in session
app.jinja_env.globals.update(is_authenticated=is_authenticated)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")


@app.route("/U1ReadingComprehension1")
def U1ReadingComprehension1():
    if is_authenticated():
        googleAccountName = session['name']
        response = requests.get(f'https://people.googleapis.com/v1/people/{session["google_id"]}?personFields=photos&key={api_key}')
        profile_pic_url = response.json()['photos'][0]['url']
        return render_template("U1-ReadingComprehension1.html", googleAccname=googleAccountName, profile_pic=profile_pic_url)