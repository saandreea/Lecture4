import os
from flask import Flask, render_template, request
from models import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_PATRU")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
  # Select all.
  # flights = Flight.query.all()

  # Select where origin = "Paris", limit 1.
  # flights = Flight.query.filter_by(origin="Paris").first()

  # Select where origin = "Paris".
  # flights = Flight.query.filter_by(origin="Paris")
  # for flight in flights:
  #   print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes.")

  # flights = Flight.query.filter_by(origin="Paris").count()
  # print(flights)

  # Select where id = 4:
  # flight = Flight.query.get(4)
  # print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes, where id is {flight.id}.")

  # SElect order by origin
  # flights = Flight.query.order_by(Flight.origin.desc()).all()
  # for flight in flights:
  #   print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes.")

  # Select where origin not Paris.
  # flights = Flight.query.filter(Flight.origin != "Paris").all()
  # for flight in flights:
  #   print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes.")

  # Select origin like %a%
  # flights = Flight.query.filter(Flight.origin.like("%o%")).all()
  # for flight in flights:
  #   print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes.")

  # Select from flights where origin in ("Tokyo", "Paris")
  # flights = Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()
  # for flight in flights:
  #   print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes.")

  # Select from flights where origin = "Paris" or duration > 500
  # flights = Flight.query.filter(or_(Flight.origin == 'Paris', Flight.duration >540))
  # for flight in flights:
  #   print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes.")

  # Select from flights join passengers on flights.id = passengers.flight_id;
  flights = db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
  for flight in flights:
    print(flight.Flight.origin, flight.Flight.destination, flight.Flight.duration, flight.Passenger.name) 

if __name__ == "__main__":
  with app.app_context():
    main()