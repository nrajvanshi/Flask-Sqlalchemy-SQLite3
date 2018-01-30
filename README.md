# Flask-Sqlalchemy-SQLite3
Post and Get Curls: Accessing data from database using Flask+SQLAlchemy
Using car.py, we can connect to sqlite3 database using flask-sqlalchemy. This python script includes code structure for connection to a database in order to facilitate creation of an object 'car' that would contain data contained in csv file car_info.csv.
This script also includes code structure for getting all records from database and for adding new record into the database.
Apart from this a seperate ddl and dml has been included to show creation of table and data loading from csv in Sqlite3.
car_info.csv is the csv datafile

NOTE: Code is not working and is failing with following error: TypeError: <car "2017-06-01 00:00:00"> is not JSON serializable
