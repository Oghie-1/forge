#!/usr/bin/python3
from datetime import datetime, timedelta
from .service_criteria import ServiceCriteria

class MileageServiceCriteria(ServiceCriteria):
    def __init__(self, mileage_threshold_days):
        self.mileage_threshold = timedelta(days=mileage_threshold_days)

    def check_service(self, current_mileage, last_service_mileage):
        mileage_difference = current_mileage - last_service_mileage
        """Check if the mileage difference exceeds the threshold"""
        return mileage_difference > self.mileage_threshold