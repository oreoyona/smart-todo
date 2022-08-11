from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost:5432'

db = SQLAlchemy(server)


migrate = Migrate(server, db)


class Student(db.Model):
    __tablename__ = 'allstudents'
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    post_name = db.Column(db.String(50), nullable=False)
    graduating = db.Column(db.Boolean, nullable=False, default=False)
    
    
    def __init__(self, name, post_name, graduating):
        self.name = name
        self.post_name = post_name
        self.graduating = graduating

    def __repr__(self):
        return f"student_id: {self.id} | name: {self.name} | post_name: {self.post_name}"



# listItem = Student.query.all()

    
@server.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html><head><title>Response</title></head>
    <body style="background-color: brown;">
    <button> CLick me to say hello</button>
    </body>
    </html>
    """ 
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
   server.run(FLASK_DEBUG=True)




