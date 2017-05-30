import os
from flask import Flask
app = Flask(__name__)

try:
    developMode = os.environ['PYTHON_ENV'] == 'development'
except KeyError:
    print "No environment mode set, defaulting to production"
    developMode = False

@app.route("/")
def hello():
    return "Hello,  World!"

if __name__ == "__main__":
    app.run(debug=developMode,host='0.0.0.0')
