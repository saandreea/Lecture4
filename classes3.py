class Flight:
  counter = 1
  def __init__(self, origin, destination, duration):
    # Details about flight.
    self.origin = origin
    self.destination = destination
    self.duration = duration

    # Keep track of id number.
    self.id = Flight.counter
    Flight.counter += 1

    # Keep track of passengers.
    self.passengers = []

  def add_passenger(self, p):
    self.passengers.append(p)
    p.flight_id = self.id

  def delay(self, amount):
    self.duration += amount

  def print_info(self):
    print(f"Flight id: {self.id}")
    print(f"Flight origin: {self.origin}")
    print(f"Flight destination: {self.destination}")
    print(f"Flight duration: {self.duration}")
    print()
    print("Passengers:")
    for passenger in self.passengers:
      print(f"{passenger.name} and {passenger.flight_id}")

class Passenger:
  def __init__(self, name):
    self.name = name

def main():

  # Create flights.
  f1 = Flight("New York", "Paris", 540)
  f2 = Flight("Bucharest", "Doha", 260)

  # Create passengers.
  alice = Passenger("Alice")
  bob = Passenger("Bob")
  andreea = Passenger("Andreea")
  cristi = Passenger("Cristi")

  # Add passengers.
  f1.add_passenger(alice)
  f1.add_passenger(bob)
  f2.add_passenger(andreea)
  f2.add_passenger(cristi)

  f1.print_info()
  f2.print_info()

if __name__ == "__main__":
  main()

  






  
 
