import sys
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_migrate import Migrate
from models.todo import Todo, db
from forms.new_todo import New_todo

import config

def create_app(env):
    server = Flask(__name__, template_folder='templates')
    server.config.from_object(env)
    db.init_app(server)
    return server


server = create_app(config)
server.app_context().push()

migrate = Migrate(server, db)


    
@server.route('/')
def index():
   return render_template('home.html', title='s/todo')


    
@server.route('/todo')
def new_todo():
    form = New_todo()
    return render_template("forms/new_todo.html", form=form, title='add todo')

 
@server.route('/todo', methods=['POST'])    
def save_todo():
    new_todo = New_todo(request.form)
    todo = Todo()
    try:
        new_todo.populate_obj(todo)
        db.session.add(todo)
        db.session.commit()
        flash("The new Todo was added")
            
    except:
            print(sys.exc_info) 
            flash("Something went wrong")  
            db.sesson.rollback() 
            
    finally:
            db.session.close()
            
    return render_template("home.html", title='home')







if __name__ == '__main__':
   server.run(host="0.0.0.0")




