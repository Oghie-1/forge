#!/usr/bin/python3
from abc import ABC
"""Import the Engine class from the engine module"""
from engine import Engine 


class SternmanEngine(Engine):
    """
    A concrete class representing Sternman engines that inherit from the Engine class.
    This class checks if the engine should be serviced based on a warning light status.
    """

    def __init__(self, last_service_date, warning_light_is_on):
        """
        Constructor for SternmanEngine instances.

        Args:
            last_service_date (datetime.date): The date when the engine was last serviced.
            warning_light_is_on (bool): True if the warning light is on, False otherwise.
        """
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        """
        Check if the engine should be serviced based on the status of the warning light.

        Returns:
            bool: True if the engine should be serviced, False otherwise.
        """
        return self.warning_light_is_on

"""This class represents a specific type of engine and inherits from the Engine class."""