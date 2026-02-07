from . import db 
#from . is importing from the current package import db

from flask_login import UserMixin
#helps us logs users in, user object inherits from usermixin

from sqlalchemy.sql import func
#to let flask do the date stuff for us 

#Creating our tables:
class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)#db software sets uniques ID, usually + 1 
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now )#func.now gets current DT
    
    #How to associate this note for the user:
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #foreign key means we must pass a valid id of an existing user to this column
    #One ID/User has many notes so we use ForeignKey
    #We could have a note belonging to lots of users 
    #user.id as its the user table and its their id
    #Foreignkey text is lowercase





class User(db.Model, UserMixin):#inherits those two classes
#defining the layout for user now
    id = db.Column(db.Integer, primary_key = True)   #all objects in a database have a primary key, a unique ID, usually an integer
    #so for the column its an integer, this is a primary key

    email = db.Column(db.String(150), unique=True)#unique means no duplicates

    password = db.Column(db.String(150))

    first_name = db.Column(db.String(150))

    notes = db.relationship('Note')#tells flask/sql alch, every time we create a note store it where we keep all their notes
    #relationships is the same case as your class

#this is for our database models basically