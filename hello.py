# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, Hello Flask, Hello Dima!' 

if __name__ == '__main__':
    app.run(host='0.0.0.0')

