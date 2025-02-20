import unittest
from models.route import Route
from models.truck import Truck
from models.package import Package
from datetime import timedelta

VALID_DEPARTURE = "2025-02-21-09:00"
VALID_START_LOC = "Sydney"
VALID_NEXT_LOC = "Melbourne Brisbane"

VALID_TRUCK = "Man"
VALID_ID = 1
VALID_CAPACITY = 37000
VALID_MAX_RANGE= 10000

VALID_CUSTOMER_NAME = "Uasim"
VALID_PHONE = "0404040404"
VALID_CSTART_LOC = "Sydney"
VALID_CEND_LOC = "Melbourne"
VALID_WEIGHT = 45

class Truck_Should(unittest.TestCase):

    def test_route_initialization(self):
        route = Route(VALID_DEPARTURE, VALID_START_LOC, VALID_NEXT_LOC)
        self.assertEqual(route.departure_time, VALID_DEPARTURE)
        self.assertEqual(route.locations[0], VALID_START_LOC)
        self.assertEqual(route.locations[1], VALID_NEXT_LOC)
    
    def test_total_distance(self):
        route = Route(VALID_DEPARTURE, VALID_START_LOC, VALID_NEXT_LOC)
        self.assertEqual(route.total_distance, 2642)
    
    def test_assign_truck(self):
        route = Route(VALID_DEPARTURE, VALID_START_LOC, VALID_NEXT_LOC)
        truck = Truck(VALID_ID, VALID_TRUCK, VALID_CAPACITY, VALID_MAX_RANGE)
        route.assign_truck(truck)
        self.assertEqual(route.assigned_truck, truck)
    
    def test_assign_package(self):
        package = Package(VALID_CUSTOMER_NAME, VALID_PHONE, VALID_CSTART_LOC, VALID_CEND_LOC, VALID_WEIGHT)
        initial_len = len(self.route.packages)
        self.route.assign_package(package)
        self.assertEqual(len(self.route.packages), initial_len + 1)
        self.assertEqual(str(self.route.packages[-1]), package)
    
    def test_calculate_arrival_times(self):
        expected_times = [
            self.departure_time,
            self.departure_time + timedelta(hours=1),
            self.departure_time + timedelta(hours=2)
        ]
        self.assertEqual(self.route.arrival_times, expected_times)
    
    def test_current_and_next_stop(self):
        self.assertEqual(self.route.current_stop(self.departure_time), 'A')
        self.assertEqual(self.route.next_stop(self.departure_time), 'B')

        time_between_A_B = self.departure_time + timedelta(minutes=30)
        self.assertEqual(self.route.current_stop(time_between_A_B), 'A')
        self.assertEqual(self.route.next_stop(time_between_A_B), 'B')

        time_between_B_C = self.departure_time + timedelta(hours=1, minutes=30)
        self.assertEqual(self.route.current_stop(time_between_B_C), 'B')
        self.assertEqual(self.route.next_stop(time_between_B_C), 'C')

        time_after_route = self.departure_time + timedelta(hours=3)
        self.assertEqual(self.route.current_stop(time_after_route), 'C')
        self.assertEqual(self.route.next_stop(time_after_route), 'C')
    
    def test_str_representation(self):
        expected_time_A = self.departure_time.strftime("%b %d %H:%M")
        expected_time_B = (self.departure_time + timedelta(hours=1)).strftime("%b %d %H:%M")
        expected_time_C = (self.departure_time + timedelta(hours=2)).strftime("%b %d %H:%M")
        expected_str = (
            f"Route 1 -> A ({expected_time_A}) -> B ({expected_time_B}) -> C ({expected_time_C})"
        )
        self.assertEqual(str(self.route), expected_str)
