import unittest
from datetime import datetime, timedelta
from models.locations import Locations
from models.package import Package
from models.truck import Truck
from models.route import Route

class TestRoute(unittest.TestCase):

    def setUp(self):
        
        Locations.locations = [
            "Sydney", "Melbourne", "Adelaide",
            "AliceSprings", "Brisbane", "Darwin", "Perth"
        ]
        
        Route.ID = 1
        Package.ID = 1

        self.departure_time = datetime(2025, 2, 20, 8, 0, 0)

        self.route = Route(self.departure_time, "Sydney", "Melbourne", "Adelaide")

    def test_initialization(self):
        self.assertEqual(self.route.locations, ["Sydney", "Melbourne", "Adelaide"])
        self.assertEqual(self.route.id, 1)
        self.assertIsNone(self.route.assigned_truck)
        self.assertEqual(self.route.packages, [])

    def test_total_distance(self):
        expected_distance = 877 + 725
        self.assertEqual(self.route.total_distance(), expected_distance)

    def test_assign_truck(self):
        truck = Truck(1001,"Scania", 42000,8000)
        self.route.assign_truck(truck)
        self.assertEqual(self.route.assigned_truck, truck)
        with self.assertRaises(ValueError):
            self.route.assign_truck(truck)

    def test_assign_package(self):
        package = Package("John Doe", "0412345678", "Sydney", "Adelaide", 100)
        self.assertEqual(len(self.route.packages), 0)
        self.route.assign_package(package)
        self.assertEqual(len(self.route.packages), 1)
        self.assertEqual(self.route.packages[0], package)

    def test_calculate_arrival_times(self):
        arrival_times = self.route.arrival_times
        self.assertEqual(len(arrival_times), len(self.route.locations))
        self.assertEqual(arrival_times[0], self.departure_time)
        travel_hours = 877 / Route.AVERAGE_SPEED_KMH
        expected_melbourne_time = self.departure_time + timedelta(hours=travel_hours)
        self.assertAlmostEqual(
            arrival_times[1].timestamp(),
            expected_melbourne_time.timestamp(),
            delta=1
        )

    def test_current_stop(self):
        t0 = self.departure_time
        t1 = self.route.arrival_times[1]
        t2 = self.route.arrival_times[2]

        mid_leg1 = t0 + (t1 - t0) / 2
        self.assertEqual(self.route.current_stop(mid_leg1), "Sydney")

        mid_leg2 = t1 + (t2 - t1) / 2
        self.assertEqual(self.route.current_stop(mid_leg2), "Melbourne")

        after_route = t2 + timedelta(hours=1)
        self.assertEqual(self.route.current_stop(after_route), "Adelaide")

    def test_next_stop(self):
        t0 = self.departure_time
        t1 = self.route.arrival_times[1]
        t2 = self.route.arrival_times[2]

        before_route = t0 - timedelta(minutes=5)
        self.assertEqual(self.route.next_stop(before_route), "Sydney")

        mid_leg1 = t0 + (t1 - t0) / 2
        self.assertEqual(self.route.next_stop(mid_leg1), "Melbourne")

        mid_leg2 = t1 + (t2 - t1) / 2
        self.assertEqual(self.route.next_stop(mid_leg2), "Adelaide")

        after_route = t2 + timedelta(hours=1)
        self.assertEqual(self.route.next_stop(after_route), "Adelaide")

    def test_str(self):
        parts = []
        for loc, time in zip(self.route.locations, self.route.arrival_times):
            time_str = time.strftime("%b %d %H:%M")
            parts.append(f"{loc} ({time_str})")
        expected_str = f"Route {self.route.id} -> " + " -> ".join(parts)
        self.assertEqual(str(self.route), expected_str)
