#!/usr/bin/python3
from datetime import datetime

from engine.capulet_engine import CapuletEngine

from batteries.spindler_battery import SpindlerBattery

from model.carmodel import CarModel

from abc import ABC, abstractmethod

from engine.base.carpart import CarPart

from engine.base.service_criteria import *


"""
    service criteria implementations"""



class ServiceCriteria(ABC):
    @abstractmethod
    def check_service(self):
        pass



class MileageServiceCriteria(ServiceCriteria):
    def __init__(self, mileage_threshold):
        self.mileage_threshold = mileage_threshold

    def check_service(self, current_mileage, last_service_mileage):
        return current_mileage - last_service_mileage > self.mileage_threshold


class TimeServiceCriteria(ServiceCriteria):
    def __init__(self, time_threshold_years):
        self.time_threshold_years = time_threshold_years

    def check_service(self, current_date, last_service_date):
        return (current_date - last_service_date).days > self.time_threshold_years * 365
