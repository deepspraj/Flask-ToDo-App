# To-Do Web Application

A simple server side to-do task application based on flask micro-framework.

### Demo

[Heroku](https://todo-app-deepspraj.herokuapp.com/) Platform

### Use of language's

1. Python
2. SQLite (SQLAlchemy)
3. Javascript (Minor)
4. HTML
5. CSS

### For test purpose :
- Username : temp
- Password : temp@123

### Password Information:

Password's are hashed before saving to database.

## Running Locally

Make sure you have [Python](https://www.python.org/) and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed.

```sh

git clone https://github.com/deepspraj/flask-todo-app.git # or clone your own fork
cd flask-todo-app.
pip install -r requirements.txt
python app.py
```

Your app should now be running on [http://localhost:5000](http://localhost:5000/).

<br>

## Deploying to Heroku
```
git add .
git commit -am "realease v1"
git push heroku master
heroku open
```

Alternatively, you can deploy your own copy of the app using this button:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Setting up sqlite:
- Delete migrations folder, database and follow steps given below.
(use if any changes are to be implemented in  database else don't perform ever)

```
(terminal) > set FLASK_APP=app.py
(terminal) > flask db init
(terminal) > flask db migrate
(terminal) > flask db upgrade
```
