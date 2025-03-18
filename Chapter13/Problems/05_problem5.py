# explore the flask module and create a web server using flask and python
# flask is used to make websites and api
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run() #to run the app we use this 