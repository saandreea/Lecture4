import os
from models import *
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_PATRU")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
  flight = Flight.query.get(4)
  db.session.delete(flight)
  db.session.commit()


if __name__ == "__main__":
  with app.app_context():
    main()