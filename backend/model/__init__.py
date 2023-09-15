#!/usr/bin/python3
from datetime import datetime

from engine.capulet_engine import CapuletEngine

from batteries.spindler_battery import SpindlerBattery

from model.carmodel import CarModel

from abc import ABC, abstractmethod

from engine.base.carpart import CarPart

from engine.base.service_criteria import *

from model.carfactory import *

# Example usage
if __name__ == "__main__":
    # Create service criteria instances
    mileage_criteria = MileageServiceCriteria(30000)
    time_criteria = TimeServiceCriteria(4)

    # Create car models with different parts and service criteria
    thovex_parts = [("Engine", mileage_criteria), ("Battery", time_criteria)]
    thovex_model = CarFactory.create_model("Thovex", thovex_parts)

    # Simulate current date and last service date
    current_date = datetime(2023, 1, 1)
    thovex_model.parts[0].last_service_date = datetime(2020, 1, 1)
    thovex_model.parts[1].last_service_date = datetime(2019, 1, 1)

    # Check if the car model needs service
    if thovex_model.needs_service(current_date):
        print(f"{thovex_model.name} needs service.")
    else:
        print(f"{thovex_model.name} does not need service.")
