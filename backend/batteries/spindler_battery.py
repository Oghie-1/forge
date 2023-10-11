#!/usr/bin/python3


"""Import the Battery class from the battery module"""
from backend.batteries.battery import Battery


"""Import the add_years_to_date function from the utils module"""
from backend.utils import add_years_to_date


class SpindlerBattery(Battery):
    """
    A concrete class representing Spindler batteries that inherit from the Battery class.
    This class checks if the battery needs service based on service date criteria.
    """

    def __init__(self, current_date, last_service_date):
        """
        Constructor for SpindlerBattery instances.

        Args:
            current_date (datetime.date): The current date.
            last_service_date (datetime.date): The date when the battery was last serviced.
        """
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        """
        Check if the battery needs service based on a service date criterion.

        Returns:
            bool: True if the battery needs service, False otherwise.
        """
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)

        # Check if the date when the battery should be serviced is earlier than the current date
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False

# This class represents a specific type of battery and inherits from the Battery class.
