#!/usr/bin/python3

"""Import the Serviceable abstract class"""

from backend.serviceable import Serviceable


class Car(Serviceable):
    """
    A concrete class representing a car that inherits from the Serviceable abstract class.
    This class checks if the car needs service based on its engine and battery.
    """

    def __init__(self, engine, battery):
        """
        Constructor for Car instances.

        Args:
            engine (Engine): The engine of the car.
            battery (Battery): The battery of the car.
        """
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        """
        Check if the car needs service based on both engine and battery criteria.

        Returns:
            bool: True if the car needs service, False otherwise.
        """
        # Call the needs_service method of the parent class (Serviceable)
        # and combine it with the needs_service method of the battery.
        return super().needs_service() or self.battery.needs_service()

"""This class represents a car that can be checked for serviceability."""
