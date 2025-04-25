from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from cohere_api import test
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = "hello"

# Use PostgreSQL if DATABASE_URL is set, otherwise fallback to SQLite
database_url = os.environ.get("DATABASE_URL")
if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    images = db.relationship('images', backref='user', lazy=True)


class images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image_base64 = db.Column(db.Text)
    caption = db.Column(db.String(255))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

@app.route("/home", methods = ['POST', 'GET'])
def home():
    if 'email' not in session:
        flash('You need to login first')
        return redirect('/login')
    
    user_email = session['email']
    user = users.query.filter_by(email=user_email).first()
    user_id=user.id
    user_images = images.query.filter_by(user_id=user_id).all()
    # serialized_images = [{'base64': img.image_base64,
    #                                  'latitude': img.latitude,
    #                                  'longitude': img.longitude,
    #                                  'caption': img.caption} for img in user_images]
    
    # serialized_images = json.dumps(serialized_images)


    if request.method == 'GET':
        if "email" in session:
            return render_template('index.html', user_images=user_images)
        
        else:
            flash("Please log in")
            return redirect(url_for("login"))
   
    if request.method == 'POST':
        array = []
 
        for type, id in request.form.items():
            array.append(id)
            print(array)

        temp = test(array[1])
        array.pop(1)
        array.extend(temp)

        new_image = images(
            user_id=user.id,
            image_base64=array[0],
            caption=array[1],
            latitude=array[2],
            longitude=array[3]
        )

        db.session.add(new_image)
        db.session.commit()

        flash("Image added successfully")
        return redirect(url_for("home"))

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        email = request.form["emailInput"]
        password = request.form["passwordInput"]
        print(email, password)
        existing_user = users.query.filter_by(email=email).first()
        if existing_user:
            flash("Already logged in")
            session["email"] = email
            print(session)
            return redirect(url_for("home"))

        new_user = users(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        session["email"] = email
        print(session)
        return redirect("login")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        email = request.form["emailInput"]
        password = request.form["passwordInput"]

        found_user = users.query.filter_by(email=email, password=password).first()
        
        if not email or not password:
            flash('Email and password are required')
            return redirect('/login')

        if found_user:
            session["email"] = found_user.email
            flash("Login Succesful!")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password")
            return redirect(url_for("login"))

    else:
        if "email" in session:
            flash("Already logged in")
            return redirect(url_for("home"))
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    if "email" in session:
        email = session["email"]
        flash(f"You have been logged out, {email}", "info")
    session.pop("email", None)
    return redirect(url_for("login"))

@app.route("/view")
def view():
    # if 'email' not in session:
    #     flash('You need to login first')
    #     return redirect('/login')
    # user_email = session['email']
    # user = users.query.filter_by(email=user_email).first()
    # user_id=user.id
    # user_images = images.query.filter_by(user_id=user_id).all()
    return render_template("view.html", users=users.query.all(), images=images.query.all())

@app.route("/db_info")
def db_info():
    database_type = "PostgreSQL" if "postgresql" in str(db.engine.url) else "SQLite"
    return f"Database type: {database_type}, Connection: {db.engine.url}"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
