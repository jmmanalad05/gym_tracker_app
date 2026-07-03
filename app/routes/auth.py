from flask import Blueprint, request, render_template, redirect, flash
from app.extensions.db import Database
from werkzeug.security import generate_password_hash

auth_bp = Blueprint("auth", __name__)
db = Database()


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    # Get form data
    firstName = request.form["firstName"]
    lastName = request.form["lastName"]
    email = request.form["email"]
    phone = request.form["phone"]
    username = request.form["username"]
    password = request.form["password"]
    confirmPassword = request.form["confirmPassword"]

    # 1. PASSWORD CHECK
    if password != confirmPassword:
        flash("Passwords do not match!", "error")
        return redirect("/register")

    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)

    # 2. CHECK DUPLICATES
    cursor.execute("""
        SELECT * FROM users
        WHERE email = %s OR username = %s OR phone = %s
    """, (email, username, phone))

    existing_user = cursor.fetchone()

    if existing_user:
        flash("Email, username, or phone already exists!", "error")
        conn.close()
        return redirect("/register")

    # 3. HASH PASSWORD
    hashed_password = generate_password_hash(password)

    # 4. INSERT USER
    cursor.execute("""
        INSERT INTO users (firstName, lastName, email, phone, username, passwordHash)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (firstName, lastName, email, phone, username, hashed_password))

    conn.commit()
    conn.close()

    flash("Registration successful!", "success")
    return redirect("/login")