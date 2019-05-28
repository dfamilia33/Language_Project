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
* SqlLite
* Development Database: TBA

## How it works
Each word has a class that holds information about the word so a user can browse words based on criteria(timestamp,country, popularity,
etc..). That class inherits from a databse model so it can easily store itself in a database file. As of now testing is being done
through a linux ubuntu command line until deployment

## Launch
To Launch from a linux command line:

* source venv/Scripts/activate
* export FLASK_APP=app/language.py
* flask run


## Credits

SVG flags made by [koppi](https://github.com/koppi) along with CSS integration credited to [lipis](https://github.com/lipis).
