from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# These lines of code are setting up the Flask application and configuring the SQLAlchemy database
# connection.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    complete = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def index():
    allTodos = Todo.query.all()
    return  render_template('index.html', allTodos = allTodos)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')
    todo = Todo(title = title, desc =desc, complete = False)
    db.session.add(todo)
    db.session.commit()
    allTodos = Todo.query.all()
    return  redirect(url_for("index"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    allTodos = Todo.query.filter_by(sno = todo_id).first()
    print(allTodos)
    allTodos.complete = not allTodos.complete
    db.session.commit()
    return  redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    allTodos = Todo.query.filter_by(sno = todo_id).first()
    db.session.delete(allTodos)
    db.session.commit()
    
    return  redirect(url_for("index"))


if __name__ == '__main__':
    app.run(port=8000, debug=True)
