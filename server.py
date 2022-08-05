from distutils.debug import DEBUG
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost:5432'

db = SQLAlchemy(server)


class Student(db.Model):
    __tablename__ = 'allstudents'
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    post_name = db.Column(db.String(50), nullable=False)

    def __init__(self, id, name, post_name):
        self.id = id
        self.name = name
        self.post_name = post_name

    def __repr__(self):
        return f"student_id: {self.id} | name: {self.name} | post_name: {self.post_name}"




    
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
@server.route('/lists')
def show_all():
    return render_template('index.html', tbleau=[0,1,2,3])
    
    
if __name__ == '__main__':
   server.run(host="0.0.0.0")
   server(DEBUG=True)