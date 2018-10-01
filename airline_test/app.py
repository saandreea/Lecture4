from models import *
import os
from flask import Flask, render_template, request

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_PATRU")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
  flights = Flight.query.all()
  return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
  if not request.form.get("name"):
    return render_template("message.html", headline="Error!", message="No passenger name.")
  name = request.form.get("name").capitalize()

  try:
    flight_id = int(request.form.get("flight_id"))
  except ValueError:
    return render_template("message.html", headline="Error!", message="No such flight id.")
  
  flight = Flight.query.filter_by(id=flight_id)

  if flight is None: 
    return render_template("message.html", headline="Error!", message="No such flight.")

  passenger = Passenger(name=name, flight_id=flight_id)
  db.session.add(passenger)
  db.session.commit()
  return render_template("message.html", headline="Success!", message="You have successfully booked a flight")

@app.route("/flights")
def flights():
  flights = Flight.query.all()
  return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
  zbor = Flight.query.get(flight_id)
  if zbor is None: 
    return render_template("message.html", headline="Error!", message="No such flight.")

  passengers = zbor.passengers
  return render_template("flight.html", flight=zbor, passengers=passengers)