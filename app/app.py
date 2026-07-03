# Project: Gym App

# Main Objective: Allow users to track their workout sessions.
# Register and Login Features.

from flask import Flask, render_template, request, redirect, flash, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)


@app.route("/")
def home():
    return render_template("index.html")
