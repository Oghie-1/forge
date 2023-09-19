#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock
from datetime import datetime, timedelta, date
from backend.car import Car
from backend.carFactory import carFactory
from backend.serviceable import Serviceable
from backend.utils import add_years_to_date

"""Import Battery base and types"""
from batteries.battery import Battery
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

"""Import Engine base and types"""
from backend.engines.engine import Engine
from backend.engines.capulet_engine import CapuletEngine
from backend.engines.sternman_engine import SternmanEngine
from backend.engines.willoughby_engine import WilloughbyEngine




"""Test Battery module"""

class TestBattery(unittest.TestCase):

    def test_abstract_battery_creation(self):
        # Attempt to create an instance of the abstract Battery class (should raise TypeError)
        with self.assertRaises(TypeError):
            battery = Battery()


"""Test for nubin_battery"""
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


class TestSpindlerBattery(unittest.TestCase):

    def test_needs_service_true(self):
        # Create an instance of the SpindlerBattery class with a last service date 2 years ago
        last_service_date = date.today().replace(year=date.today().year - 2)
        current_date = date.today()
        spindler_battery = SpindlerBattery(current_date, last_service_date)

        # Check if the battery needs service (should return True)
        self.assertTrue(spindler_battery.needs_service())

    def test_needs_service_false(self):
        # Create an instance of the SpindlerBattery class with a last service date less than 2 years ago
        last_service_date = date.today().replace(year=date.today().year - 1)
        current_date = date.today()
        spindler_battery = SpindlerBattery(current_date, last_service_date)

        # Check if the battery needs service (should return False)
        self.assertFalse(spindler_battery.needs_service())


"""Test Engine Module"""


class TestEngine(unittest.TestCase):

    def test_abstract_engine_creation(self):
        """Atempt to create an instance of the abstract Battery Class
        return: a type error
        """
        with self.assertRaises(TypeError):
            engine = Engine()

"""tEST cAPULATE engine"""
class TestCapuletEngine(unittest.TestCase):

    def test_needs_service_true(self):
        # Create an instance of the CapuletEngine class with current mileage 30000 greater than last service mileage
        last_service_date = datetime(2022, 1, 1)
        current_mileage = 60000
        last_service_mileage = 30000
        capulet_engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)

        # Check if the engine needs service (should return True)
        self.assertTrue(capulet_engine.needs_service())

    def test_needs_service_false(self):
        # Create an instance of the CapuletEngine class with current mileage less than 30000 greater than last service mileage
        last_service_date = datetime(2022, 1, 1)
        current_mileage = 40000
        last_service_mileage = 10000
        capulet_engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)

        # Check if the engine needs service (should return False)
        self.assertFalse(capulet_engine.needs_service())

"""Test cases for sternman_engines"""


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        # Create an instance of the SternmanEngine class with the warning light on
        last_service_date = datetime(2022, 1, 1)
        warning_light_is_on = True
        sternman_engine = SternmanEngine(
            last_service_date, warning_light_is_on)

        # Check if the engine needs service (should return True)
        self.assertTrue(sternman_engine.needs_service())

    def test_needs_service_false(self):
        # Create an instance of the SternmanEngine class with the warning light off
        last_service_date = datetime(2022, 1, 1)
        warning_light_is_on = False
        sternman_engine = SternmanEngine(
            last_service_date, warning_light_is_on)

        # Check if the engine needs service (should return False)
        self.assertFalse(sternman_engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service_true(self):
        # Create an instance of the WilloughbyEngine class with current mileage 60,000 greater than last service mileage
        last_service_date = datetime(2022, 1, 1)
        current_mileage = 100000
        last_service_mileage = 40000
        willoughby_engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)

        # Check if the engine needs service (should return True)
        self.assertTrue(willoughby_engine.needs_service())

    def test_needs_service_false(self):
        # Create an instance of the WilloughbyEngine class with current mileage less than 60,000 greater than last service mileage
        last_service_date = datetime(2022, 1, 1)
        current_mileage = 50000
        last_service_mileage = 10000
        willoughby_engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)

        # Check if the engine needs service (should return False)
        self.assertFalse(willoughby_engine.needs_service())

"""Test car by creating mock engines"""


class TestCar(unittest.TestCase):

    def test_needs_service_true(self):
        # Create mock engine and battery objects
        mock_engine = MagicMock()
        mock_engine.needs_service.return_value = True
        mock_battery = MagicMock()
        mock_battery.needs_service.return_value = True

        # Create an instance of the Car class with the mock engine and battery
        car = Car(mock_engine, mock_battery)

        # Check if the car needs service (should return True)
        self.assertTrue(car.needs_service())

    def test_needs_service_false(self):
        # Create mock engine and battery objects
        mock_engine = MagicMock()
        mock_engine.needs_service.return_value = False
        mock_battery = MagicMock()
        mock_battery.needs_service.return_value = False

        # Create an instance of the Car class with the mock engine and battery
        car = Car(mock_engine, mock_battery)

        # Check if the car needs service (should return False)
        self.assertFalse(car.needs_service())


"""Test CarFactory tonverify the creation of diff models car with various engines"""


class TestCarFactory(unittest.TestCase):

    def test_create_calliope(self):
        # Create a Calliope car using the factory method
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        current_mileage = 50000
        last_service_mileage = 20000
        car = carFactory.create_calliope(
            current_date, last_service_date, current_mileage, last_service_mileage)

        # Verify that the car is an instance of the Car class
        self.assertIsInstance(car, Car)

    def test_create_glissade(self):
        # Create a Glissade car using the factory method
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        current_mileage = 60000
        last_service_mileage = 30000
        car = carFactory.create_glissade(
            current_date, last_service_date, current_mileage, last_service_mileage)

        # Verify that the car is an instance of the Car class
        self.assertIsInstance(car, Car)

    def test_create_palindrome(self):
        # Create a Palindrome car using the factory method
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        warning_light_is_on = True
        car = carFactory.create_palindrome(
            current_date, last_service_date, warning_light_is_on)

        # Verify that the car is an instance of the Car class
        self.assertIsInstance(car, Car)

    def test_create_rorschach(self):
        # Create a Rorschach car using the factory method
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        current_mileage = 40000
        last_service_mileage = 10000
        car = carFactory.create_rorschach(
            current_date, last_service_date, current_mileage, last_service_mileage)

        # Verify that the car is an instance of the Car class
        self.assertIsInstance(car, Car)

    def test_create_thovex(self):
        # Create a Thovex car using the factory method
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2022, 1, 1)
        current_mileage = 30000
        last_service_mileage = 10000
        car = carFactory.create_thovex(
            current_date, last_service_date, current_mileage, last_service_mileage)

        # Verify that the car is an instance of the Car class
        self.assertIsInstance(car, Car)

"""Test Serviceable method"""


class TestServiceable(unittest.TestCase):

    def test_abstract_needs_service(self):
        """Attempt to create an instance of the abstract Serviceable Class should raise a TypeError"""
        with self.assertRaises(TypeError):
            serviceable = Serviceable()

""" Test add_"""


class TestAddYearsToDate(unittest.TestCase):

    def test_add_years_to_date(self):
        # Test adding 3 years to a date
        original_date = date(2020, 1, 1)
        years_to_add = 3
        expected_date = date(2023, 1, 1)
        result_date = add_years_to_date(original_date, years_to_add)
        self.assertEqual(result_date, expected_date)

    def test_add_negative_years_to_date(self):
        # Test adding -2 years to a date (subtracting 2 years)
        original_date = date(2020, 1, 1)
        years_to_add = -2
        expected_date = date(2018, 1, 1)
        result_date = add_years_to_date(original_date, years_to_add)
        self.assertEqual(result_date, expected_date)


if __name__ == '__main__':
    unittest.main()
