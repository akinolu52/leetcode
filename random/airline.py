import uuid


class Airline:

    def __init__(self, name=None):
        self._name = name
        self._booked = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def book(self, passenger, plane, cls=None):
        while cls not in ['first class', 'coach']:

            cls = input("Please pick a seat: First class or Coach ").lower()

            if cls not in ['first class', 'coach']:
                print("Please select either from 'first class' or 'coach'")

        choice = None
        if cls == 'first class':
            first_class = list(enumerate(plane.capacity))[:10]
            while choice not in range(10):
                try:
                    choice = int(
                        input("Please select a number between 0 and 9 for your seats: "))
                except ValueError:
                    print("Please select a valid number between 0 and 9")
                if choice in self._booked:
                    print(f"That seat is taken please choose another seat\n"
                          f"These seats are booked: {self._booked}")
                    choice = None
            for seat in first_class:
                if seat[0] == choice:
                    self._extracted_from_book_24(passenger, plane, seat)
        else:
            coach = list(enumerate(plane.capacity))[10:50]
            while choice not in range(10, 50):
                try:
                    choice = int(
                        input(
                            "Please select a number between 10 and 50 for your seats: "
                        )
                    )
                except ValueError:
                    print("Please select a valid number between 10 and 50")
                if choice in self._booked:
                    print(f"That seat is taken please choose another seat\n"
                          f"These seats are booked: {self._booked}")
                    choice = None
            for seat in coach:
                if seat[0] == choice:
                    self.coach_seat(passenger, plane, seat)

    def coach_seat(self, passenger, plane, seat):
        plane.capacity[seat[1]] = passenger
        passenger._balance = passenger._balance - seat[1].price
        self._booked.append(seat[0])
        passenger._assignment = f"{seat[1].tier} seat {seat[0]}"

    def refund(self, passenger, plane):
        for i, (seat, person) in enumerate(plane.capacity.items()):
            if person == passenger:
                plane.capacity[seat] = None
                passenger._balance = passenger._balance + seat.price
                passenger._assignment = None
                self._booked.remove(i)


class Passenger:

    def __init__(self, name, balance=1000, assignment=None):
        self.id = uuid.uuid1()
        self.name = name
        self._balance = balance
        self._assignment = assignment

    def get_balance(self):
        return self._balance

    def get_assignment(self):
        return self._assignment


class Seat:

    def __init__(self):
        pass


class FirstClass(Seat):

    def __init__(self):
        super().__init__()
        self.tier = 'First Class'
        self.price = 500


class Coach(Seat):

    def __init__(self):
        super().__init__()
        self.tier = 'Coach'
        self.price = 100


class Plane:

    def __init__(self):
        self.capacity = {}
        temp_capacity = [FirstClass() for _ in range(10)]
        temp_capacity.extend(Coach() for _ in range(10, 50))
        for seat in temp_capacity:
            # Each seat has no value(person) assigned
            self.capacity[seat] = None

    def view_plane(self):
        for i, k in self.capacity.items():
            print(f"{i} : {k}")

    def get_available_seats(self):
        return sum(value is None for value in self.capacity.values())
