#!/usr/bin/python3
from datetime import datetime
from models.carpart import CarPart
from service_criteria.service_criteria import *

""""
carmodel class

"""


class CarModel:
    def __init__(self, name):
        self.name = name
        self.parts = []

    def add_part(self, part_name, service_criteria):
        part = CarPart(part_name, service_criteria)
        self.parts.append(part)

    def needs_service(self, current_date):
        for part in self.parts:
            if part.service_criteria.check_service(current_date, part.last_service_date):
                return True
        return False
