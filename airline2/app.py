from models import *
from flask import Flask, render_template, request
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_PATRU")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
  flights = Flight.query.all()
  return render_template("index.html", flights = flights)

@app.route("/book", methods=["POST"])
def book():
  
  if not request.form.get("name"):
    return render_template("message.html", message="Missing passenger name.", headline="Error!")
  name = request.form.get("name")

  try:
    flight_id = int(request.form.get("flight_id"))
  except ValueError:
    return render_template("message.html", message="Missing flight number.", headline="Error!")

  flight = Flight.query.filter_by(id = flight_id)
  if flight is None:
    return render_template("message.html", message="No such flight.", headline="Error!")

  passenger = Passenger(name=name, flight_id=flight_id)
  db.session.add(passenger)
  db.session.commit()
  return render_template("message.html", message="You have booked a flight!", headline="Success!")

@app.route("/flights")
def flights():
  flights = Flight.query.all()
  return render_template("flights.html", flights = flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
  flight = Flight.query.filter_by(id=flight_id)
  passengers = Passenger.query.filter_by(flight_id=flight_id)
  return render_template("flight.html", passengers=passengers, flight=flight)