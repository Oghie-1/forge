#!/usr/bin/python3
from datetime import datetime
from backend.engines.capulet_engine import CapuletEngine
from backend.batteries.spindler_battery import SpindlerBattery


class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False