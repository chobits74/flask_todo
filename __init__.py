
from flask import Flask
from flask import render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret Admirer"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db3.sqlite'
db = SQLAlchemy(app)

#class MyDateTime(db.TypeDecorator):
 # impl = db.DateTime

  #  def process_bind_param(self,value, dialect):
   #     if type(value) is str:
    #        return datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
     #   return value


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, default=datetime.now)
    #due = db.Column(db.Date,nullable = True, default=datetime.now) 
    done = db.Column(db.Boolean)

#create constructor
def __init__(self, name,done):
    self.name = name
    #add if task is done
    self.done = done
    
#route section
@app.route('/')
def index():
    todo_list = Data.query.all()
    return render_template('index.html', todo_list = todo_list)

@app.route('/insert', methods =['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name'] #using html form not flask wtf form
        #due = request.form['due']   
          
#constructor
        my_data = Data(name=name, done=False)
        db.session.add(my_data)
        db.session.commit()
        return redirect (url_for('index'))

@app.route('/delete/<int:todo_id>', methods =['POST', 'GET'])
def delete(todo_id):
    todo = Data.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect (url_for('index'))

@app.route('/done/<int:todo_id>', methods = ['POST', 'GET'])
def done(todo_id):
    todo = Data.query.filter_by(id=todo_id).first()
    todo.done = not todo.done
    db.session.commit()
    return redirect (url_for('index'))




if __name__ == '__main__':
    db.create_all()


    app.run(debug=True)
    #row.due.strftime('%Y-%m-%d')
