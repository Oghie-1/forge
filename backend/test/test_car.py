#!/usr/bin/python3
import unittest
from datetime import datetime, timedelta

from batteries.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):

    def setUp(self):
        # Define a current date and a last service date for testing
        self.current_date = datetime(2023, 9, 16)
        self.last_service_date = datetime(2019, 9, 16)

    def test_needs_service_true(self):
        # Create an instance of the NubbinBattery class with a last service date exactly 4 years ago
        nubbin_battery = NubbinBattery(
            self.last_service_date, self.current_date)

        # Check if the battery needs service (should return True)
        self.assertTrue(nubbin_battery.needs_service())

    def test_needs_service_false(self):
        # Create an instance of the NubbinBattery class with a last service date less than 4 years ago
        last_service_date = datetime(2022, 9, 16)
        nubbin_battery = NubbinBattery(last_service_date, self.current_date)

        # Check if the battery needs service (should return False)
        self.assertFalse(nubbin_battery.needs_service())

    def test_needs_service_edge_case(self):
        # Create an instance of the NubbinBattery class with a last service date 4 years and 1 day ago
        last_service_date = self.current_date - timedelta(days=4*365 + 1)
        nubbin_battery = NubbinBattery(last_service_date, self.current_date)

        # Check if the battery needs service (should return True)
        self.assertTrue(nubbin_battery.needs_service())

    def test_needs_service_same_year(self):
        # Create an instance of the NubbinBattery class with a last service date in the same year
        last_service_date = datetime(2023, 2, 16)
        nubbin_battery = NubbinBattery(last_service_date, self.current_date)

        # Check if the battery needs service (should return False)
        self.assertFalse(nubbin_battery.needs_service())

    def test_needs_service_future_date(self):
        # Create an instance of the NubbinBattery class with a last service date in the future
        last_service_date = datetime(2024, 9, 16)
        nubbin_battery = NubbinBattery(last_service_date, self.current_date)

        # Check if the battery needs service (should return False)
        self.assertFalse(nubbin_battery.needs_service())


if __name__ == '__main__':
    unittest.main()
