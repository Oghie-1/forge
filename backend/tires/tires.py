#!/usr/bin/python3


from abc import ABC, abstractmethod
"""Defines an abstract base class called Tires"""


class Tires(ABC):

    """Constructor for the Tire class. Currently, it does nothing."""

    def __init__(self):
        pass

    """Äbstract method declaration for "need_service".
        This method should be implemented by subclasses to specify how a Tire checks if it needs service.
        By using the @abstractmethod decorator, we enforce that subclasses must provide an implementation.
            This abstract class serves as a blueprint for creating concrete tire classes."""

    @abstractmethod
    def need_service(self):
        pass
