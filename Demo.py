class Flight:
    def __init__(self, flight_number, destination, seats_available):
        self.flight_number = flight_number
        self.destination = destination
        self.seats_available = seats_available

    def book_seat(self):
        if self.seats_available > 0:
            self.seats_available -= 1
            return True
        return False

    def cancel_seat(self):
        self.seats_available += 1

    def __str__(self):
        return f"Flight {self.flight_number} to {self.destination} - Seats Available: {self.seats_available}"


class ReservationSystem:
    def __init__(self):
        self.flights = []
        self.reservations = {}

    def add_flight(self, flight_number, destination, seats):
        flight = Flight(flight_number, destination, seats)
        self.flights.append(flight)

    def show_flights(self):
        for flight in self.flights:
            print(flight)

    def book_ticket(self, passenger_name, flight_number):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                if flight.book_seat():
                    self.reservations[passenger_name] = flight_number
                    print(f"Booking confirmed for {passenger_name} on flight {flight_number}")
                else:
                    print("Sorry, no seats available.")
                return
        print("Flight not found.")

    def cancel_ticket(self, passenger_name):
        if passenger_name in self.reservations:
            flight_number = self.reservations.pop(passenger_name)
            for flight in self.flights:
                if flight.flight_number == flight_number:
                    flight.cancel_seat()
                    print(f"Reservation for {passenger_name} on flight {flight_number} has been cancelled.")
                    return
        print("No reservation found.")

system = ReservationSystem()

num_flights = int(input("Enter the number of flights: "))
for _ in range(num_flights):
    flight_number = input("Enter flight number: ")
    destination = input("Enter destination: ")
    seats = int(input("Enter number of seats: "))
    system.add_flight(flight_number, destination, seats)

while True:
    print("\n1. Show Flights\n2. Book Ticket\n3. Cancel Ticket\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        system.show_flights()
    elif choice == "2":
        passenger_name = input("Enter passenger name: ")
        flight_number = input("Enter flight number: ")
        system.book_ticket(passenger_name, flight_number)
    elif choice == "3":
        passenger_name = input("Enter passenger name: ")
        system.cancel_ticket(passenger_name)
    elif choice == "4":
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
