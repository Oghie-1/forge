#!/usr/bin/python3
"""Import the abstract base class module"""
from abc import ABC, abstractmethod  


class Serviceable(ABC):
    """
    An abstract base class representing a serviceable entity.
    
    Subclasses of this class must implement the 'needs_service' method.
    """

    @abstractmethod
    def needs_service(self):
        """
        Determine whether the entity needs service.

        This method must be implemented by concrete subclasses.

        Returns:
            bool: True if the entity needs service, False otherwise.
        """
        pass

"""This abstract class serves as a blueprint for creating concrete serviceable classes."""