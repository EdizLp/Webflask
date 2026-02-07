from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()#making a db
DB_NAME = "database.db"


def create_app():

    app = Flask(__name__) # to initialise flask 

    #config is a dictionary-like object to store my secret settings
    app.config['SECRET_KEY'] = 'hecarim' #secures the cookie and session data - never share it 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'#my sql database is located here
    db.init_app(app)#telling it we're using this flask app for the database


    #look in the current folder for these two folders, import them. 
    from .views import views
    from .auth import auth
    
    #registering blueprints 
    app.register_blueprint(views, url_prefix='/')#telling main these exist and contain routes
    app.register_blueprint(auth, url_prefix='/')#url prefix tells me where do i need to go to access its routes


    from .models import User, Note

    create_database(app)
    
    return app #returned the app

def create_database(app):
    if not path.exists('website/' + DB_NAME): #create the db if it doesn't exist
        with app.app_context():
            db.create_all()
        print('Created Database!')