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


    
@server.route('/todo', methods=['GET', 'POST'])
def new_todo():
    form = New_todo()
    if request.method == 'POST':
        try:
        
            
            form = New_todo(request.form)
            todo = Todo(
                title=form.data['title'],
                description=form.data['description'],
                project=form.data['project']
            )
            db.session.add(todo)
            db.session.commit()
            db.session.close()
            flash("The new Todo was added")
            
        except:
            print(sys.exc_info) 
            flash("Something went wrong")  
            db.sesson.rollback() 
            
        finally:
            db.session.close()
            
            
    elif request.method == 'GET':
        return render_template("forms/new_todo.html", form=New_todo(), title='add todo')
    
    return render_template("home.html")
    
    

if __name__ == '__main__':
   server.run(host="0.0.0.0")




