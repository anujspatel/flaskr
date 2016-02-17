from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/projects/')
def projects():
    return 'lets go man'

if __name__ == '__main__':
    app.run(debug=True)

/flaskr
    /static
    /templates