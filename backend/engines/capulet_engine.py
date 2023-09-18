#!/usr/bin/python3
from datetime import datetime
from abc import ABC
from backend.engines.engine import Engine


class CapuletEngine(Engine):
    """
    A concrete class representing Capulet engines that inherit from the Engine class.
    This class checks if the engine should be serviced based on mileage criteria.
    """

    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        """
        Constructor for CapuletEngine instances.

        Args:
            last_service_date (datetime.date): The date when the engine was last serviced.
            current_mileage (int): The current mileage of the engine.
            last_service_mileage (int): The mileage of the engine at the last service.
        """
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        print("Initialization completed!!")

    def needs_service(self):
        """
        Check if the engine should be serviced based on mileage criteria.

        Returns:
            bool: True if the engine should be serviced, False otherwise.
        """
        return self.current_mileage - self.last_service_mileage >= 30000

"""This class represents a specific type of engine and inherits from the Engine class."""