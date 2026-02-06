from flask import Flask


def create_app():
    app = Flask(__name__) # to initialise flask 
    app.config['SECRET_KEY'] = 'hecarim' #secures the cookie and session data - never share it 

    #look in the current folder for these two folders, import them. 
    from .views import views
    from .auth import auth
    
    #registering blueprints 
    app.register_blueprint(views, url_prefix='/')#telling main these exist and contain routes
    app.register_blueprint(auth, url_prefix='/')#url prefix tells me where do i need to go to access its routes

    return app #returned the app