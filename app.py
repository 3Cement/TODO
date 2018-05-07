from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
#file_path = os.path.abspath(os.getcwd())+"\todo.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'todo.db')

db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200))
	complete = db.Column(db.Boolean)

@app.route('/')	
def index():
	return render_template('index.html')

@app.route('/add', methods=['POST'])

if __name__ == '__main__':
	app.run(debug=True)
