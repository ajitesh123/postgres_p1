from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app config is a directory with all caps
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ajitesh@localhost:5432/persondb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
#Link an instance of database (db) with the flask app (app)

class Person(db.Model):
    __tablename__='persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    #Customise the print output
    def __repr__(self):
        return f"<Person ID: {self.id}, Name: {self.name}>"

db.create_all()
#detects model and creates tables for them (if they don't exit)

@app.route('/')
def hello_world():
    person = Person.query.first()
    return f"Hello World, {person.name}!\n"
