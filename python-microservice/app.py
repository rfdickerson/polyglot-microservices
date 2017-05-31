import os
import requests

from flask import Flask
app = Flask(__name__)

try:
    developMode = os.environ['PYTHON_ENV'] == 'development'
except KeyError:
    print "No environment mode set, defaulting to production"
    developMode = False

@app.route("/")
def hello():
    return "Hello  World from Python!"

@app.route("/call/node")
def call_node():
    r = requests.get('http://node-microservice:3000/')
    return "Python service received: \"{0}\"".format( r.text)

@app.route("/call/swift")
def call_swift():
    r = requests.get("http://swift-microservice:8090/")
    return "Python service received: \"{0}\"".format( r.text)

if __name__ == "__main__":
    app.run(debug=developMode,host='0.0.0.0')
