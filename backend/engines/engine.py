#!/usr/bin/python3

"""Import the abstract base class module"""
from abc import ABC, abstractmethod


class Engine(ABC):
    """
    An abstract base class representing an engine that needs service.

    This class defines the abstract method 'needs_service', which must be implemented by subclasses.
    """

    @abstractmethod
    def needs_service(self):
        """
        Determine whether the engine needs service.

        Returns:
            bool: True if the engine needs service, False otherwise.
        """
        pass

# This abstract class serves as a blueprint for creating concrete engine classes.
