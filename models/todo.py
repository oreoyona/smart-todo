
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'Todo'
    id = db.Column('todo_id', db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(300))
    project = db.Column(db.String(100))
    
    # def __init__(self, title, description, project):
    #     self.title = title
    #     self.description = description
    #     self.project = project

    def __repr__(self):
        return f"id: {self.id} | title: {self.title} | post_name: {self.description} | project: {self.project}"


class Project(db.Model):
    id = db.Column('todo_project_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    todo_id = db.Column(db.Integer, db.ForeignKey("Todo.todo_id"), nullable=True)
    todo_title = db.relationship("Todo", backref=db.backref("todos"))
    
    
class Category(db.Model):
    id = db.Column('todo_project_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)