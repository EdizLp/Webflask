from flask import Blueprint, render_template, request, flash, redirect, url_for
#this file is for authentication
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user #for logging in users, current user works with usermixin

auth = Blueprint('auth', __name__)#this defines our blueprint, basically saying a different sector of my code



@auth.route('/login', methods = ['GET', 'POST'])#these are the types of requests we accept. By default its get only 
def login():
    if request.method =='POST':#so we are requesting a sign in, not just on the page
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email ).first() #looking for entries in our database, only first result
        if user:
            if check_password_hash(user.password, password):#hash their password and then check it
                flash('Logged in successfully!', category = 'success')
                login_user(user, remember = True) #until they clear their session they stayed logged in
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')
    return render_template("login.html", user = current_user) #this is our html, well in this case our template, you can even pass variables with Jinja 
#you can run variables to each template for them to use with jinja
@auth.route('/logout')
@login_required #decorator, this makes sure they can't access this page if they aren't locked in 
def logout():
    logout_user()#self explanatory 
    return redirect(url_for("auth.login"))

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        email = request.form.get('email') #If we have a post request, get the form from the request, specifically the email (the name)
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email = email).first()

        if user:#same email
            flash('Email Already Exists', category='error')

        elif len(email) < 4:#validate email length because that definitely says whether its valid lmao
            flash('Email must be greater than 3 characters.', category = 'error')#category name doesnt matter
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category = 'error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category = 'error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category = 'error')
        else:  #add user to database
            new_user = User(email = email, first_name = firstName, password = generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category = 'success')#so u can add more categories using this category stuff
            login_user(user, remember = True)
            return redirect(url_for('views.home'))#finds what url maps to the function home, could do just / but if u change it its fucked
            #(blueprintname.functionname)

    return render_template("sign_up.html", user = current_user)

