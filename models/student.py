from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

