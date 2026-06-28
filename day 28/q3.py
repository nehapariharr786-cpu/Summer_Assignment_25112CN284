tickets = []

def book_ticket():
    name = input("Enter Passenger Name: ")
    seat = int(input("Enter Seat Number: "))

    ticket = {
        "Passenger": name,
        "Seat": seat
    }

    tickets.append(ticket)
    print("Ticket Booked Successfully")


def cancel_ticket():
    seat = int(input("Enter Seat Number: "))

    for t in tickets:
        if t["Seat"] == seat:
            tickets.remove(t)
            print("Ticket Cancelled")
            return

    print("Ticket not found")


def show_ticket():
    print(tickets)


while True:
    print("\nTicket Booking System")
    print("1.Book Ticket")
    print("2.Cancel Ticket")
    print("3.Show Tickets")
    print("4.Exit")

    ch=int(input("Choice: "))

    if ch==1:
        book_ticket()
    elif ch==2:
        cancel_ticket()
    elif ch==3:
        show_ticket()
    else:
        break
    