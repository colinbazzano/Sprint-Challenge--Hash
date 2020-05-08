#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"{self.source} - {self.destination}"


cache = {}


def reconstruct_trip(tickets, length):
    route = [None] * length  # allocate memory
    for ticket in tickets:
        cache[ticket] = (ticket.source, ticket.destination)
        print("Ticket:", ticket)
    curr_ticket = cache["NONE"]
    print("CURR:", curr_ticket)
    for i in range(length):
        if i > 0:
            source = route[i-1]
        else:
            # source = "NONE"
            source = "NONE"
        cache[source] = route[i]

    return route[:-1]


tickets = [
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
]

print(reconstruct_trip(tickets, 10))
