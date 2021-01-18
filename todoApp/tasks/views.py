from flask import Flask, Blueprint,render_template,redirect,url_for, flash, request
from flask_login import login_required, current_user
from .forms import createTask
from todoApp.models import User, tasks
from todoApp import db
from datetime import date

task = Blueprint('task', __name__)



@task.route('/allTask')
def allTask():

    everyTask = tasks.query.all()
    admin = 'deepspraj'
    user1 = ''
    user2 = ''
    total = len(everyTask)
    return render_template('allTask.html', everyTask=everyTask, user1=user1, user2=user2, total=total, admin=admin)
    


@task.route('/separate')
@login_required
def separate():

    Id = request.args.get('tag')
    separateTask = tasks.query.get(Id)


    return render_template('separateTask.html', separateTask=separateTask)

@task.route('/delete')
@login_required
def delete():

    Id = request.args.get('Id')
    separateTask = tasks.query.get(Id)
    db.session.delete(separateTask)
    db.session.commit()

    return redirect('allTask')

@task.route('/createTask', methods=['GET', 'POST'])
@login_required
def newTask():

    form = createTask()

    if form.validate_on_submit():

        if form.dateOfTask.data >= date.today():
            
            taskNew = tasks(task = form.taskname.data, date = form.dateOfTask.data, userId=current_user.id)

            db.session.add(taskNew)
            db.session.commit()
            flash("Successfully Created task")

        return redirect(url_for('core.home'))
    

    return render_template('createTask.html', form = form)