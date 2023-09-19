#!/usr/bin/python3

"""Import from the engine module"""
from backend.engines.capulet_engine import CapuletEngine
from backend.engines.sternman_engine import SternmanEngine
from backend.engines.willoughby_engine import WilloughbyEngine

"""Import battery module"""
from backend.batteries.nubbin_battery import NubbinBattery
from backend.batteries.spindler_battery import SpindlerBattery

"""Import car module"""
from backend.car import Car

last_service_mileage = 35000

class carFactory(Car):
    """
    A factory class for creating different types of cars with specific engines and batteries.
    """

    def __init__(self, engine, battery):
        """
        Constructor for carFactory instances.

        Args:
            engine (Engine): The engine for the car.
            battery (Battery): The battery for the car.
        """

        self.engine = engine
        self.battery = battery
    

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        """
        Create a Calliope car with a CapuletEngine and a SpindlerBattery.

        Args:
            current_date (datetime.date): The current date.
            last_service_date (datetime.date): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage of the car at the last service.

        Returns:
            Car: The created Calliope car.
        """

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        """
        Create a Glissade car with a WilloughbyEngine and a SpindlerBattery.

        Args:
            current_date (datetime.date): The current date.
            last_service_date (datetime.date): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage of the car at the last service.

        Returns:
            Car: The created Glissade car.
        """

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        """
        Create a Palindrome car with a SternmanEngine and a SpindlerBattery.

        Args:
            current_date (datetime.date): The current date.
            last_service_date (datetime.date): The date when the car was last serviced.
            warning_light_is_on: only when engine needs service

        Returns:
            Car: The created Palindrome car.
        """

        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        """
        Create a Rorschach car with a CapuletEngine and a SpindlerBattery.

        Args:
            current_date (datetime.date): The current date.
            last_service_date (datetime.date): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage of the car at the last service.

        Returns:
            Car: The created Rorschach car.
        """

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        """
        Create a Thovex car with a CapuletEngine and a SpindlerBattery.

        Args:
            current_date (datetime.date): The current date.
            last_service_date (datetime.date): The date when the car was last serviced.
            current_mileage (int): The current mileage of the car.
            last_service_mileage (int): The mileage of the car at the last service.

        Returns:
            Car: The created Thovex car.
        """

        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    

"""This factory class provides convenient methods for creating different car models."""