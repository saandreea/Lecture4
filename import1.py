from models import *
import sqlalchemy
from flask import Flask, render_template, request
import os
import csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_PATRU")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
  f = open("flights.csv")
  reader = csv.reader(f)

  for origin, destination, duration in reader:
    flight = Flight(origin = origin, destination = destination, duration = duration)
    db.session.add(flight)
    print(f"Added {origin} to {destination} lasting {duration} minutes.")
  db.session.commit()
   


if __name__ == "__main__":
  with app.app_context():
    main()

