#!/usr/bin/python3

from service_criteria.service_criteria import ServiceCriteria


class TimeServiceCriteria(ServiceCriteria):
    def __init__(self, time_threshold_years):
        self.time_threshold_years = time_threshold_years

    def check_service(self, current_date, last_service_date):
        return (current_date - last_service_date).days > self.time_threshold_years * 365
