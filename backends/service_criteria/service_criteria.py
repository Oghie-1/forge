#!/usr/bin/python3
from abc import ABC, abstractmethod


class ServiceCriteria(ABC):
    @abstractmethod
    def check_service(self):
        pass
