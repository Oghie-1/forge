#!/usr/bin/python3

"""ïmport modules"""
from models.car import Car
from datetime import datetime, timedelta
from engines.capulet_engine import CapuletEngine
from batteries.spindler_battery import SpindlerBattery
from models.carmodel import CarModel
from service_criteria.mileage_criteria import MileageServiceCriteria
from service_criteria.time_criteria import TimeServiceCriteria
from models.carfactory import CarFactory

"""Example usage here..."""



if __name__ == "__main__":
    """Create service criteria instances"""
    mileage_criteria = MileageServiceCriteria(3000)
    time_criteria = TimeServiceCriteria(4)

    """Create car models with different parts and service criteria"""
    thovex_parts = [("Engine", mileage_criteria), ("Battery", time_criteria)]
    thovex_model = CarFactory.create_model("Thovex", thovex_parts)

    """ Simulate current date and last service date """
    current_date = datetime(2023, 1, 1)
    thovex_model.parts[0].last_service_date = datetime(2020, 1, 1)
    thovex_model.parts[1].last_service_date = datetime(2019, 1, 1)

    #debug

    print(f"\nCurrent Mileage: {thovex_model.parts[0].current_mileage}")
    print(f"\nLast Service Mileage: {thovex_model.parts[0].last_service_mileage}")
    print(f"\nMileage Threshold: {thovex_model.parts[0].service_criteria.mileage_threshold}\n")


    """ Check if the car model needs service"""
    if thovex_model.needs_service(current_date):
        print(f"{thovex_model.name} needs service.")
    else:
        print(f"{thovex_model.name} does not need service.")
