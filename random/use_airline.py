from airline import Airline, Coach, FirstClass, Passenger, Plane, Seat

plane = Plane()
p = Passenger("Egazi")
p2 = Passenger("Tosin")
p3 = Passenger("Victor")
airline = Airline("Australia Airline")


plane.view_plane()

airline.book(p, plane)
airline.book(p2, plane)
print(airline._booked)
print(f"passenger 1 balance: {p.get_balance()}\n"
      f"passenger 1 assignment: {p.get_assignment()}\n"
      f"passenger 2 balance: {p2.get_balance()}\n"
      f"passenger 2 assignment: {p2.get_assignment()}\n"
      f"Number of seats available: {plane.get_available_seats()}\n"
      f"Number of seats booked: {len(airline._booked)}")
plane.view_plane()
airline.book(p3, plane)
plane.view_plane()
print("--------------")
print(airline._booked)
print(f"passenger 1 balance: {p.get_balance()}\n"
      f"passenger 1 assignment: {p.get_assignment()}\n"
      f"passenger 2 balance: {p2.get_balance()}\n"
      f"passenger 2 assignment: {p2.get_assignment()}\n"
      f"passenger 3 balance: {p3.get_balance()}\n"
      f"passenger 3 assignment: {p3.get_assignment()}\n"
      f"Number of seats available: {plane.get_available_seats()}\n"
      f"Number of seats booked: {len(airline._booked)}")
print("----------------")
airline.refund(p2, plane)
print(airline._booked)
print(f"passenger 1 balance: {p.get_balance()}\n"
      f"passenger 1 assignment: {p.get_assignment()}\n"
      f"passenger 2 balance: {p2.get_balance()}\n"
      f"passenger 2 assignment: {p2.get_assignment()}\n"
      f"passenger 3 balance: {p3.get_balance()}\n"
      f"passenger 3 assignment: {p3.get_assignment()}\n"
      f"Number of seats available: {plane.get_available_seats()}\n"
      f"Number of seats booked: {len(airline._booked)}")
