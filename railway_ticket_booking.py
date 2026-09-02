import random
import string


# -----------------------------
# Sample Train Data
# -----------------------------
trains = {
    "12301": {
        "name": "Howrah Rajdhani Express",
        "from": "Howrah",
        "to": "New Delhi",
        "fare": 1850,
        "seats": 50
    },
    "12302": {
        "name": "Kolkata Duronto Express",
        "from": "Howrah",
        "to": "Mumbai",
        "fare": 1650,
        "seats": 40
    },
    "12841": {
        "name": "Coromandel Express",
        "from": "Howrah",
        "to": "Chennai",
        "fare": 1450,
        "seats": 45
    },
    "12021": {
        "name": "Shatabdi Express",
        "from": "Howrah",
        "to": "Bhubaneswar",
        "fare": 950,
        "seats": 35
    }
}


# Stores all bookings
bookings = {}


# -----------------------------
# Generate PNR
# -----------------------------
def generate_pnr():
    while True:
        pnr = "".join(random.choices(string.digits, k=10))

        if pnr not in bookings:
            return pnr


# -----------------------------
# Display Train List
# -----------------------------
def show_trains():
    print("\n" + "=" * 75)
    print("                         AVAILABLE TRAINS")
    print("=" * 75)

    for number, train in trains.items():
        print(f"""
Train Number : {number}
Train Name   : {train['name']}
Route        : {train['from']} -> {train['to']}
Fare         : ₹{train['fare']}
Available    : {train['seats']} seats
{"-" * 75}""")


# -----------------------------
# Book Ticket
# -----------------------------
def book_ticket():
    show_trains()

    train_number = input("\nEnter Train Number: ").strip()

    if train_number not in trains:
        print("\nInvalid train number.")
        return

    train = trains[train_number]

    if train["seats"] <= 0:
        print("\nSorry! No seats are available.")
        return

    print("\nEnter Passenger Details")

    name = input("Passenger Name: ").strip()
    age = input("Age: ").strip()
    gender = input("Gender: ").strip()

    if not name or not age or not gender:
        print("\nAll passenger details are required.")
        return

    try:
        age = int(age)

        if age <= 0:
            print("\nPlease enter a valid age.")
            return

    except ValueError:
        print("\nAge must be a number.")
        return

    pnr = generate_pnr()

    bookings[pnr] = {
        "name": name,
        "age": age,
        "gender": gender,
        "train_number": train_number,
        "train_name": train["name"],
        "from": train["from"],
        "to": train["to"],
        "fare": train["fare"]
    }

    trains[train_number]["seats"] -= 1

    print("\n" + "=" * 50)
    print("             TICKET BOOKED SUCCESSFULLY ✅")
    print("=" * 50)
    print(f"PNR Number : {pnr}")
    print(f"Passenger  : {name}")
    print(f"Train      : {train['name']}")
    print(f"Route      : {train['from']} -> {train['to']}")
    print(f"Fare       : ₹{train['fare']}")
    print("=" * 50)


# -----------------------------
# Search Booking
# -----------------------------
def search_booking():
    pnr = input("\nEnter PNR Number: ").strip()

    if pnr not in bookings:
        print("\nNo booking found with this PNR.")
        return

    booking = bookings[pnr]

    print("\n" + "=" * 60)
    print("                  BOOKING DETAILS")
    print("=" * 60)
    print(f"PNR Number  : {pnr}")
    print(f"Passenger   : {booking['name']}")
    print(f"Age         : {booking['age']}")
    print(f"Gender      : {booking['gender']}")
    print(f"Train No.   : {booking['train_number']}")
    print(f"Train Name  : {booking['train_name']}")
    print(f"From        : {booking['from']}")
    print(f"To          : {booking['to']}")
    print(f"Fare        : ₹{booking['fare']}")
    print("=" * 60)


# -----------------------------
# Cancel Ticket
# -----------------------------
def cancel_ticket():
    pnr = input("\nEnter PNR Number to cancel: ").strip()

    if pnr not in bookings:
        print("\nNo booking found with this PNR.")
        return

    booking = bookings[pnr]

    trains[booking["train_number"]]["seats"] += 1

    del bookings[pnr]

    print("\nTicket cancelled successfully.")
    print(f"PNR {pnr} has been cancelled.")


# -----------------------------
# Main Menu
# -----------------------------
def main():
    while True:
        print("\n" + "=" * 55)
        print("          RAILWAY TICKET BOOKING SYSTEM")
        print("=" * 55)
        print("1. Show Available Trains")
        print("2. Book Ticket")
        print("3. Search Booking by PNR")
        print("4. Cancel Ticket")
        print("5. Exit")
        print("=" * 55)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_trains()

        elif choice == "2":
            book_ticket()

        elif choice == "3":
            search_booking()

        elif choice == "4":
            cancel_ticket()

        elif choice == "5":
            print("\nThank you for using Railway Ticket Booking System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    main()