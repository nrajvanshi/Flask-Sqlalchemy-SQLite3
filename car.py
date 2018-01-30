from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from numpy import genfromtxt

app = Flask(__name__, template_folder='/home/nikita')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class car(db.Model):
   make = db.Column(db.String(20))
   model = db.Column(db.String(15))
   year = db.Column(db.Integer) 
   chasis_id = db.Column(db.String(15))
   id = db.Column(db.Integer)
   last_update=db.Column(db.String(20), primary_key=True)
   price = db.Column(db.Float)

def __init__(self):
   self.make = make
   self.model = model
   self.year = year
   self.chasis_id = chasis_id
   self.id=id
   self.last_update=last_update
   self.price=price


#code for loading data from provided csv file 

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',',skip_header=1,converters={0: lambda s: str(s),1: lambda s: str(s),3: lambda s: str(s),5: lambda s: str(s)})
    return data.tolist()
try:
	file_name = "car_info.csv"
	data = Load_Data(file_name) 

	for i in data:
		record = car(**{
         		'make' : i[0],
                	'model' : i[1],
                	'year' : i[2],
                	'chasis_id' : i[3],
                	'id' : i[4],
                	'last_update' : i[5],
			'price' : i[6]})
	db.session.add(record)
	db.session.commit()
except:
	print("loading failed")
        db.session.rollback() #Rollback the changes on error
finally:
        db.session.close()

#Return car records
@app.route('/car')
def show_all():
   return jsonify(car.query.all())

#Create a new record in db
@app.route('/car', methods = ['POST'])
def new():
         cars = car(request.get_json())
         db.session.add(cars)
         db.session.commit()
         return 'Record was successfully added'
          

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
