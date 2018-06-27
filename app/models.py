from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='user',lazy='dynamic')

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '< User {} >'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))



class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    is_completed = db.Column(db.Boolean,default=False)
    alarm_time = db.Column(db.DateTime, index= True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def setAlarm(self,cuDate):
        self.alarm_time = cuDate

    def __repr__(self):
        return '<Task {}>'.format(self.task_name)
