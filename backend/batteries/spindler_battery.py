from abc import ABC

from car import Car

class SpindlerBattery(Car, ABC):

    """CONSTRUCTOR METHOD FOR spindler batteries"""

    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)

        """"creates instances for current_date and last_service_date"""
        self.current_date = current_date
        self.last_service_date = last_service_date

    """create service criteria for service prompt"""
    def engine_should_be_serviced(self):

        """"Calculate the difference in years between current_date and last_service_date"""
        time_difference = self.current_date.year - self.last_service_date.year

        """check if diff is equal to 4 years"""
        if time_difference == 2:
            return True
        else:
            return False
