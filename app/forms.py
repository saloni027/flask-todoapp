from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,DateField
from wtforms.validators import DataRequired,Email,EqualTo
from .models import User



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class ToDoListForm(FlaskForm):
    task_name = StringField('Task Name',validators=[DataRequired()])
    is_completed = BooleanField('Completed')
    alarm_time = DateField('Alarm at')
    submit  = SubmitField('Add Task')


class EditForm(FlaskForm):
    task_name = StringField('task_name')
    submit = SubmitField('Save me')

class DatePickerForm(FlaskForm):
    alarm_time = DateField('Alarm at', format="%m/%d/%Y")
    submit = SubmitField('Go')
