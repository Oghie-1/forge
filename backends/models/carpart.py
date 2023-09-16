#!/usr/bin/python3
from datetime import datetime
from service_criteria.service_criteria import ServiceCriteria

class CarPart:
    def __init__(self, part_name, service_criteria):
        self.part_name = part_name
        self.service_criteria = service_criteria
        self.last_service_mileage = 0 #Initialize with an appropriate value
        self.current_mileage = 0   # Initialize with an appropriate value
