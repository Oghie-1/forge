#!/usr/bin/python3

from models.carmodel import CarModel


class CarFactory:


    """factory for creating car models"""
    @staticmethod
    def create_model(model_name, parts):
        car_model = CarModel(model_name)
        for part_name, service_criteria in parts:
            car_model.add_part(part_name, service_criteria)
        return car_model
1