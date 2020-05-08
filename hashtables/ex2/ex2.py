#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"{self.source} - {self.destination}"


cache = {}


def reconstruct_trip(tickets, length):

    for ticket in tickets:
        cache[ticket.source] = ticket.destination  # set source/destination

    curr_ticket = "NONE"  # starting ticket
    route = [cache[curr_ticket]]  # make a list so we can append
    curr_ticket = cache[curr_ticket]
    while curr_ticket != "NONE":  # while we have not reached the last ticket
        route.append(cache[curr_ticket])  # add current ticket
        curr_ticket = cache[curr_ticket]

    return route


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
