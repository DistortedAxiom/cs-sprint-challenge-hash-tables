#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    dict = {}

    for ticket in tickets:
        dict[ticket.source] = ticket.destination

    current = dict["NONE"]

    for x in range(0, length):
        route.append(current)
        current = dict[current]

    return route
