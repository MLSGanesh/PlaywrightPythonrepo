# Abstraction means showing only essential features and hiding complex internal details.
# Giving access on functionality but hiding implementation.

# Example: 1

from abc import ABC, abstractmethod


class Vehicle(ABC):    # ABC: Abstract Base Class
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# concrete class implements abstract methods from abstract class
class Car(Vehicle):
    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")

# v=Vehicle() # cannot create object for abstract class
c=Car()
c.start()
c.stop()