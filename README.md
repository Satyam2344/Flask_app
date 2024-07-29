# Python_Flask_todo
THis is Flask todo list

# Install Virtual Envionment
pip install virtualenv
virtualenv env
./env/Scripts/activate.ps1
/*If there is something error then open powershell on computer and type*/
Set-ExecutionPolicy

//Always activate virtual environment before run the application
./env/Scripts/activate.ps1

# We are using SQLAlchemy, to create db :
./env/Scripts/activate.ps1
->Python
=>from app import app, db
=>app.app_context().push()
=>app.create_all()
=>exit()

# Run app

python./app.py
