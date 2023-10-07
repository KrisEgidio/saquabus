from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lines/<origin>/<destination>')
def get_lines(origin, destination):
    return ''

app.run(debug=True)
