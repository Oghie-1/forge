#!/usr/bin/env python3
from backend.utils import add_years_to_date
from backend.batteries.battery import Battery
from backend.engines.engine import Engine
from abc import ABC
from abc import ABC, abstractmethod
from datetime import datetime
from backend.tires.tires import Tires
from backend.tires.service_sensor import SensorChecker

"""
    This class represents a specific type of tire and inherits from the tire class.
"""

class CarriganTire(Tires):
    """
    A concrete class representing Carrigan Tires that inherit from the Tire  class.
    This class checks if the tires needs service based on service sensor status.
    
    """

    def __init__(self, service_sensor_status, last_service_date):
        """
        Constructor for CarriganTire instances.

        Args:
            service_sensor_status: collection of sensor array.
            last_service_array: The value of the last service array
        """

        super().__init__(last_service_date)
        self.service_sensor_status = service_sensor_status
        self.last_service_date = last_service_date
    

    def need_service(self):
        """
        Check if the tire should be serviced based on the status of the tire sensors.

        Returns:
            bool: True if the tire should be serviced, False otherwise.
        """
        sensor_service_checker = SensorChecker(self.service_sensor_status, 0.9)

        """"checks if service-sensor array is greater than 0.9, the maximum threshold for tire service"""

        if sensor_service_checker >= 0.9:
            return True
        else:
            return False
