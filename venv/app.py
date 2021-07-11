from flask import Flask

# Creating the flask app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to the game !!"


if __name__=="__main__":
    app.run()
