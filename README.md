# JeviDict 
Flask Python Project - (in Progress)

## Purpose
A dictionary web app to store collquial/slang words in the spanish language, to be able to be accessed through a varitey of filters
and sorting criteria. Meant to help those learning the language understand spoken spanish outside the classroom.

## Technologies

### Languages
* HTML
* CSS
* Python
* Javascript

### Frameworks/Technologies
* Flask
* Bootstrap
* SQLAlchemy

### Database
* Sqlite
* Production Database: TBA

## How it works
Each word has a class that holds information about the word so a user can browse words based on criteria(timestamp,country, popularity,
etc..). That class inherits from a databse model so it can easily store itself in a database file. As of now testing is being done
through a linux ubuntu command line until deployment

## Launch

Update (06/26/2019): This project has migrated from a development sqlite database to a production PostgreSQL database, and is
no longer available for a locally hosted demo. A link to a cloud hosted service of the app will be posted soon.

The app in development can be launched through a command line. This process should take
no longer than a few minutes. Start by navigting to the folder in your command line
prompt then enter the linux commands below:

To Launch from a linux command line:

Step | Command
------------ | -------------
Remove the existing virtual envrironment | rm -r venv
If you do not have virtualenv install by | pip install virtualenv
Create a virtual environment | virtualenv env
Activate Virtual envrironment | source venv/bin/activate
Dowload required packages into the env | pip install -r requirements.txt
Set the flask app variable | export FLASK_APP=app/language.py
Launch the app and enter link into browser | flask run


## Credits

SVG flags made by [koppi](https://github.com/koppi) along with CSS integration credited to [lipis](https://github.com/lipis).
