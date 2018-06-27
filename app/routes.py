from app import app,db
from flask import render_template,flash,redirect,url_for,request
from app.forms import ToDoListForm,LoginForm,RegistrationForm,EditForm,DatePickerForm
from app.models import Task,User
from flask_login import current_user,login_user,logout_user,login_required
from werkzeug.urls import url_parse
from datetime import datetime



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember = form.remember_me.data)
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('index')
        # return redirect(next_page)
        return redirect(url_for('addTask'))

    return render_template('login.html',form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('index'))


@app.route('/addTask',methods = ['GET','POST'])
@login_required
def addTask():
    form = ToDoListForm()
    if form.validate_on_submit():
        task = Task(task_name=form.task_name.data,user=current_user)
        db.session.add(task)
        db.session.commit()
        return redirect('/addTask')
    task = Task.query.filter_by(user=current_user).all()
    return render_template('to_do.html',form=form,task=task)


@app.route('/delete/<int:task_id>',methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return redirect('/')

    db.session.delete(task)
    db.session.commit()
    return redirect('/addTask')


@app.route('/done/<int:task_id>')
def done_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return redirect('/')
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True

    db.session.commit()
    return redirect('/addTask')

@app.route('/edit/<int:id>',methods = ['GET','POST'])
def edit(id):
    tsk = Task.query.get(id)
    form  = EditForm()
    if form.validate_on_submit():
        tsk.task_name = form.task_name.data
        db.session.add(tsk)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('addTask'))
    elif request.method == 'GET':
        form.task_name.data = tsk.task_name
    return render_template('edit_task.html',form=form)


@app.route('/setAlarm/<int:id>',methods = ['GET','POST'])
def setAlarm(id):
    t = Task.query.get(id)
    form = DatePickerForm()
    if form.validate_on_submit():
        t.setAlarm(form.alarm_time.data)
        db.session.commit()
        # if t.alarm_time == datetime.date.today():
        #     flash('Come on, Do the task')
        return redirect(url_for('addTask'))
    return render_template('setAlarm.html',form=form)
