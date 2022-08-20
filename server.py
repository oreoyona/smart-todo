from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect
from flask_migrate import Migrate
from models.student import Student, db



server = Flask(__name__)
db.init_app(server)
server.app_context().push()
server.config.from_object("config")


migrate = Migrate(server, db)


    
@server.route('/')
def index():
   return render_template('home.html', liste=[])

myData = []
liste = []
myPsql = Student.query.all()
@server.route('/lists')
def show_all():
    return render_template('index.html', listItem=myPsql)
    


@server.route('/add', methods=['GET', 'POST']) 
def add_stud():

    if request.method == 'POST':
        name = request.form['name']
        post_name = request.form['post_name']
        graduating = request.form.get('graduating')
        newUser = Student(id= id, name=name, post_name=post_name, graduating=graduating)
        db.session.add(newUser)
        db.session.commit()
        myData.append({'name': name, 'post_name': post_name})
        
        
        
        return redirect(url_for('show_all'))

    else:
        
        return render_template('forms.html', liste=liste)



if __name__ == '__main__':
   server.run(host="0.0.0.0")




