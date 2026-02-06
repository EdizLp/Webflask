from website import create_app #this works because of the __init__.py as it runs it all basically

app = create_app()

if __name__ == '__main__': #only if we run this file (not importing main) we execute this 
    app.run(debug=True) #if we didn't have the above it would run the web server even if u imported it, not running it
    #debug = True will rerun the webserver, saves us manually doing it


