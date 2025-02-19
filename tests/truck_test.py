import unittest

from models.truck import Truck

VALID_TRUCK = "Man"
VALID_ID = 1
VALID_CAPACITY = 37000
VALID_MAX_RANGE= 10000
class TestTruck(unittest.TestCase):

    def test_truck_initialization(self):
        truck = Truck(VALID_ID, VALID_TRUCK, VALID_CAPACITY, VALID_MAX_RANGE)
        self.assertEqual(truck.truck_id, VALID_ID)
        self.assertEqual(truck.brand, VALID_TRUCK)
        self.assertEqual(truck.capacity, VALID_CAPACITY)
        self.assertEqual(truck.max_range, VALID_MAX_RANGE)
        self.assertTrue(truck.available)

    def test_capacity_valid_value(self):
        truck = Truck(VALID_ID, VALID_TRUCK, VALID_CAPACITY, VALID_CAPACITY)
        truck.capacity = VALID_CAPACITY
        self.assertEqual(truck.capacity, VALID_CAPACITY)

    def test_capacity_negative_value(self):
        truck = Truck(VALID_ID, VALID_TRUCK, VALID_CAPACITY, VALID_CAPACITY)
        with self.assertRaises(ValueError):
            truck.capacity = -100

    def test_assign_to_route(self):
        truck = Truck(VALID_ID, VALID_TRUCK, VALID_CAPACITY, VALID_CAPACITY)
        truck.assign_to_route("Route 1")
        self.assertFalse(truck.available)

    def test_assign_to_route_when_already_assigned(self):
        truck = Truck(VALID_ID, VALID_TRUCK, VALID_CAPACITY, VALID_CAPACITY)
        truck.assign_to_route("Route 1")
        with self.assertRaises(ValueError):
            truck.assign_to_route("Route 2")

    def test_release(self):
        truck = Truck(VALID_ID, VALID_TRUCK, VALID_CAPACITY, VALID_CAPACITY)
        truck.assign_to_route("Route 1")
        truck.release()
        self.assertTrue(truck.available)

    def test_str_method(self):
        truck = Truck(VALID_ID, VALID_TRUCK, VALID_CAPACITY, VALID_CAPACITY)
        self.assertEqual(str(truck), "Truck: 1, Available: True.")