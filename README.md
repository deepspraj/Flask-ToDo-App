# To-Do Web Application

A simple server side to-do task application based on flask micro-framework.

### Demo

1. [Heroku](https://todo-app-deepspraj.herokuapp.com/) Platform
2. [PythonAnywhere](http://deepspraj.pythonanywhere.com/) Platform


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

### Setting up sqlite:
- Delete migrations folder, database and follow steps given below.
(use if any changes are to be implemented in  database else don't perform ever)

```
(terminal) > set FLASK_APP=app.py
(terminal) > flask db init
(terminal) > flask db migrate
(terminal) > flask db upgrade
```

### Starting App:
```
(terminal) > python app.py
```

### Shut Down App:

- Shut down the web app first from terminal or cmd or python-idle.
