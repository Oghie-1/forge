#!/usr/bin/python3
from datetime import datetime

from engine.capulet_engine import CapuletEngine

from batteries.spindler_battery import SpindlerBattery

from model.carmodel import CarModel

from engine.base.carpart import CarPart


class CarFactory:


    """factory for creating car models"""
    @staticmethod
    def create_model(model_name, parts):
        car_model = CarModel(model_name)
        for part_name, service_criteria in parts:
            car_model.add_part(part_name, service_criteria)
        return car_model
