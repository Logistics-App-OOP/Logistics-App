# from models.package import Package
# from datetime import *

class Route:
    ID = 0

    def __init__(self, start_loc, end_loc, est_arrival):
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.est_arrival = est_arrival
        self.route_id = Route.route_id()

    @classmethod
    def route_id(cls):
        Route.ID += 1

        return Route.ID










kurs = Route('sofai', 'bansko', '10.50')
kurs2 = Route('sofai', 'bansko', '10.50')
kurs3 = Route('sofai', 'bansko', '10.50')
kurs4 = Route('sofai', 'bansko', '10.50')

print(kurs.route_id)
print(kurs2.route_id)
print(kurs3.route_id)
print(kurs4.route_id)