from website import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True) #this ensuers the flask server is started only when this script is run directly. the debug = truethe server auto reloads when code changes and should be turned off when in production
