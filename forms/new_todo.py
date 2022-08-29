from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired



#create a new todo, whose project if not chosen will default to None
class New_todo(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description')
    project = StringField('project', default='None')
    
 
 
 #create a new project
  
class New_project(FlaskForm):
    name = StringField('name', validators=[DataRequired()])