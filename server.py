
from flask import Flask, render_template, url_for, request
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
db.create_all()
# gloire = Student(1, "Kilembi", "Chabu")
# db.session.add(gloire)
# db.session.commit()


listItem = Student.query.all()

    
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
    return render_template('index.html', listItem=listItem)
    
liste = []

@server.route('/add', methods=['GET', 'POST']) 
def add_stud():

    if request.method == 'POST':
        result = request.form
        result1 = list(result)
        liste.append(result)
        return render_template('results.html', result1= result1)

    else:
        
        return render_template('forms.html', liste=liste)



if __name__ == '__main__':
   server.run(host="0.0.0.0")
   server.run(debug=True)




