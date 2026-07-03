# Project: Gym App

# Main Objective: Allow users to track their workout sessions.
# Register and Login Features.

from flask import Flask, render_template, request, redirect, flash
from services.auth import registerUser, getUser
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        
        success = registerUser(
            request.form["firstName"],
            request.form["lastName"],
            request.form["email"],
            request.form["phone"],
            request.form["username"],
            request.form["password"],
            request.form["confirmPassword"]
        )

        if success:
            flash("Registration successful!", "success")
            return redirect("/login")

        flash("Passwords do not match.", "danger")
    return render_template("register.html")
        

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # verify user
        if getUser(username):
            print("Succesfully logged in!")
            
            return render_template("dashboard.html")
        
        else:
            return render_template("register.html")
            
            
    return render_template("login.html") 

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    
    app.run(debug=True)
    
    