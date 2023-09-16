#!/usr/bin/python3
from abc import ABC, abstractmethod
from datetime import datetime
from batteries.battery import Battery


class NubbinBattery(Battery):
    """A concrete class- This class represents a specific type of battery and inherits from the abstract Battery class."""

    def __init__(self, last_service_date, current_date):
        """
        Constructor for NubbinBattery instances.

        Args:
            last_service_date (datetime): The date when the battery was last serviced.
            current_date (datetime): The current date.
        """
        super().__init__(last_service_date)
        self.current_date = current_date

    @abstractmethod
    def engine_should_be_serviced(self):
        """
        Determine if the engine should be serviced based on the difference in years between
        the current date and the last service date.

        Returns:
            bool: True if the engine should be serviced, False otherwise.
        """
        """Calculate the difference in years between current_date and last_service_date"""
        time_difference = self.current_date.year - self.last_service_date.year

        """Check if the difference is equal to 4 years"""
        if time_difference == 4:
            return True
        else:
            return False

# 