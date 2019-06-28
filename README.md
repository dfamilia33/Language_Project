# JeviDict 
https://jevi-dict.herokuapp.com/

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
* Development: Sqlite
* Production: PostgreSQL (Current)

## How it works
Each word has a class that holds information about the word so a user can browse words based on criteria(timestamp,country, popularity,
etc..). That class inherits from a databse model so it can easily store itself in a database file. As of now testing is being done
through a linux ubuntu command line until deployment

## Launch

Update (06/26/2019): This project has migrated from a development sqlite database to a production PostgreSQL database, and is
no longer available for a locally hosted demo. A link to a cloud hosted service of the app will be posted soon.

Update (06/28/2019): The app has launched!! Visit: https://jevi-dict.herokuapp.com/

## Credits

SVG flags made by [koppi](https://github.com/koppi) along with CSS integration credited to [lipis](https://github.com/lipis).
