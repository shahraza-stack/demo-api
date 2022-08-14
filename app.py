from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/shah')
def hello_shah():
    return 'Hello shah sahab'


if __name__ == '__main__':
    app.run()
